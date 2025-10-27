#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Trading Agents Learning Engine

This script runs a learning cycle based on real-world trade data from Paradex.
It supports both automatic learning (from Paradex fills) and manual learning modes.

Automatic Mode: Fetches recent trades, matches them with past decisions,
and triggers reflection based on realized PnL.

Manual Mode: Allows manual selection of decision logs and PnL input
for targeted learning sessions.
"""

import asyncio
import json
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

from dotenv import load_dotenv

# Add project root to sys.path to allow imports from tradingagents
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.agents.utils.paradex_tools import ParadexDataManager

# --- Configuration ---
PROCESSED_FILLS_LOG = project_root / "eval_results/processed_fills.log"
DECISION_LOGS_DIR = project_root / "eval_results"

# --- Helper Functions ---

def setup_environment():
    """Load environment variables and set up output encoding."""
    load_dotenv(project_root / ".env")
    if sys.platform == 'win32':
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())
    print("[INFO] Environment setup complete.")

def load_processed_fills() -> set:
    """Reads the processed fills log and returns a set of fill IDs."""
    if not PROCESSED_FILLS_LOG.exists():
        return set()
    with open(PROCESSED_FILLS_LOG, 'r') as f:
        processed_ids = {line.strip() for line in f if line.strip()}
    print(f"[INFO] Loaded {len(processed_ids)} already processed fill IDs.")
    return processed_ids

def save_processed_fill(fill_id: str):
    """Appends a new fill ID to the processed fills log."""
    with open(PROCESSED_FILLS_LOG, 'a') as f:
        f.write(f"{fill_id}\n")

def find_decision_log(fill_timestamp_ms: int, market: str) -> Path | None:
    """Finds the decision log file corresponding to a fill."""
    # Sanitize market name to match directory structure (e.g., BTC-USD-PERP -> BTC-USD)
    sanitized_market = market.replace("-PERP", "")
    
    fill_dt = datetime.fromtimestamp(fill_timestamp_ms / 1000)
    # Search for a decision made up to 24 hours before the trade
    for i in range(2): # Check today and yesterday
        search_date = (fill_dt - timedelta(days=i)).date()
        log_dir = DECISION_LOGS_DIR / sanitized_market / "TradingAgentsStrategy_logs"
        log_file = log_dir / f"full_states_log_{search_date}.json"
        if log_file.exists():
            print(f"[INFO] Found matching decision log for {market} on {search_date}: {log_file.name}")
            return log_file
    print(f"[WARN] No decision log found for market {market} (searched in {sanitized_market}) for dates around {fill_dt.date()}")
    return None

# --- Main Learning Logic ---

async def main():
    """Main function to run the learning engine."""
    print("\n" + "="*60)
    print("      Trading Agents - Real-World Learning Engine")
    print("="*60 + "\n")
    
    setup_environment()
    paradex_manager = None
    try:
        # 1. Initialization
        paradex_manager = ParadexDataManager()
        processed_fills = load_processed_fills()

        # 2. Fetch Data from Paradex
        print("\n[STEP 1] Fetching data from Paradex...")
        history_data = await asyncio.to_thread(paradex_manager.get_trading_history, limit=100, days=30)
        
        if not history_data.get("success"):
            print(f"[ERROR] Failed to fetch trading history: {history_data.get('error')}")
            return

        all_fills = history_data.get("recent_trades", []) # Note: get_trading_history returns a dict
        if not all_fills:
            all_fills = history_data.get("analysis",{}).get("recent_trades",[])
        print(f"[SUCCESS] Fetched {history_data.get('total_trades', 0)} recent fills.")

        # 3. Find New, Unprocessed Fills
        print("\n[STEP 2] Filtering for new trades to learn from...")
        new_fills = [f for f in all_fills if f['id'] not in processed_fills]
        
        if not new_fills:
            print("[INFO] No new trades to learn from. Engine run complete.")
            return
        print(f"[SUCCESS] Found {len(new_fills)} new fills to process.")

        # 4. Instantiate the Agent Graph for its components
        print("\n[STEP 3] Initializing Agent components (Reflector & Memory)...")
        trading_agents_graph = TradingAgentsGraph()
        print("[SUCCESS] Agent components initialized.")

        # 5. Process Each New Fill
        print("\n[STEP 4] Starting reflection loop for each new trade...")
        for fill in new_fills:
            print("\n" + "-"*50)
            print(f"  Processing Fill ID: {fill['id']}")
            print(f"  Market: {fill['market']}, Side: {fill['side']}, Time: {datetime.fromtimestamp(fill['created_at']/1000)}")
            print(f"  Size: {fill['size']}, Price: {fill['price']}")
            print(f"  Realized PnL: {fill.get('realized_pnl', 'N/A')}")
            print("-"*50)

            pnl = float(fill.get('realized_pnl', 0.0))
            if pnl == 0.0:
                print("[SKIP] Fill has no realized PnL. Likely an opening trade. Skipping for now.")
                save_processed_fill(fill['id'])
                continue

            log_path = find_decision_log(fill['created_at'], fill['market'])
            if not log_path:
                print(f"[SKIP] Could not find a matching decision log for this fill. Skipping.")
                save_processed_fill(fill['id'])
                continue

            with open(log_path, 'r', encoding='utf-8') as f:
                loaded_json = json.load(f)
            
            # Handle both old and new log formats
            if loaded_json.get('decision_id'): # New format
                historical_state = loaded_json
            else: # Old, date-nested format
                historical_state = next(iter(loaded_json.values()))

            print(f"[INFO] Matched with Decision ID: {historical_state.get('decision_id', 'N/A')}")

            # d. Perform Reflection
            print("\n>>> [LEARNING] Generating reflection based on real-world trade outcome...")
            print(f">>> PnL: {pnl:.4f}")
            print(">>> Calling Reflector for each agent component...")
            
            reflections = await asyncio.to_thread(
                trading_agents_graph.reflect_on_past_decision,
                historical_state,
                pnl
            )

            # --- DETAILED LOG OUTPUT ---
            print("\n" + "-"*20 + " LESSONS LEARNED " + "-"*20)
            for component, report in reflections.items():
                print(f"\n--- Reflection on: {component.upper()} ---")
                print(report)
            print("\n" + "-"*22 + " END OF LESSONS " + "-"*21 + "\n")

            # e. Mark fill as processed
            save_processed_fill(fill['id'])
            print(f"[SUCCESS] Fill {fill['id']} processed and marked as learned.")

    except Exception as e:
        print(f"\n[FATAL ERROR] An error occurred during the learning engine run: {e}")
        import traceback
        traceback.print_exc()

    finally:
        if paradex_manager and paradex_manager.client and hasattr(paradex_manager.client, 'close'):
            paradex_manager.client.close()
        print("\n" + "="*60)
        print("      Learning Engine Run Finished")
        print("="*60 + "\n")

# --- Manual Learning Functions ---

async def manual_learning(decision_log_path: str, pnl_value: float, user_notes: str = "") -> Dict[str, Any]:
    """
    Execute manual learning based on a specific decision log and PnL value.

    Args:
        decision_log_path: Path to the decision log file
        pnl_value: The realized PnL value to use for learning
        user_notes: Optional user notes about this learning session

    Returns:
        Dictionary containing learning results and reflections
    """
    print("\n" + "="*60)
    print("      Trading Agents - Manual Learning Mode")
    print("="*60 + "\n")

    try:
        # Validate decision log file
        log_path = Path(decision_log_path)
        if not log_path.exists():
            raise FileNotFoundError(f"Decision log file not found: {decision_log_path}")

        print(f"[INFO] Loading decision log: {log_path.name}")
        print(f"[INFO] Input PnL: {pnl_value}")
        if user_notes:
            print(f"[INFO] User notes: {user_notes}")

        # Load decision log
        with open(log_path, 'r', encoding='utf-8') as f:
            log_data = json.load(f)

        # Handle different log formats
        if isinstance(log_data, dict):
            if 'decision_id' in log_data:
                historical_state = log_data
            else:
                historical_state = next(iter(log_data.values())) if log_data else {}
        else:
            raise ValueError("Invalid log data format")

        decision_id = historical_state.get('decision_id', 'Unknown')
        print(f"[INFO] Decision ID: {decision_id}")

        # Initialize trading graph
        print("\n[STEP 1] Initializing Agent components...")
        trading_agents_graph = TradingAgentsGraph()
        print("[SUCCESS] Agent components initialized.")

        # Execute reflection
        print(f"\n[STEP 2] Executing manual learning reflection...")
        print(f">>> Decision: {decision_id}")
        print(f">>> PnL: {pnl_value:.4f}")
        print(">>> Calling Reflector for each agent component...")

        reflections = await asyncio.to_thread(
            trading_agents_graph.reflect_on_past_decision,
            historical_state,
            pnl_value
        )

        # Display results
        print("\n" + "-"*20 + " MANUAL LEARNING RESULTS " + "-"*20)
        for component, report in reflections.items():
            print(f"\n--- Reflection on: {component.upper()} ---")
            print(report)
        print("\n" + "-"*25 + " END OF LESSONS " + "-"*24 + "\n")

        result = {
            'success': True,
            'decision_id': decision_id,
            'decision_log_path': str(log_path),
            'input_pnl': pnl_value,
            'user_notes': user_notes,
            'reflections': reflections,
            'timestamp': datetime.now().isoformat()
        }

        print("[SUCCESS] Manual learning completed successfully.")
        return result

    except Exception as e:
        error_msg = f"Manual learning failed: {str(e)}"
        print(f"[ERROR] {error_msg}")
        import traceback
        traceback.print_exc()

        return {
            'success': False,
            'error': error_msg,
            'timestamp': datetime.now().isoformat()
        }

def list_available_decision_logs() -> List[Dict[str, Any]]:
    """
    List all available decision logs for manual learning.

    Returns:
        List of dictionaries containing decision log information
    """
    logs = []

    try:
        # Scan all market directories
        for market_dir in DECISION_LOGS_DIR.iterdir():
            if not market_dir.is_dir():
                continue

            strategy_logs_dir = market_dir / "TradingAgentsStrategy_logs"
            if not strategy_logs_dir.exists():
                continue

            # Find all decision log files
            for log_file in strategy_logs_dir.glob("full_states_log_*.json"):
                try:
                    # Parse date from filename
                    date_str = log_file.stem.replace("full_states_log_", "")

                    # Read file to get decision info
                    with open(log_file, 'r', encoding='utf-8') as f:
                        log_data = json.load(f)

                    # Handle different log formats
                    if isinstance(log_data, dict):
                        if 'decision_id' in log_data:
                            decision_data = log_data
                        else:
                            decision_data = next(iter(log_data.values())) if log_data else {}
                    else:
                        continue

                    decision_id = decision_data.get('decision_id', 'Unknown')
                    timestamp = decision_data.get('timestamp', '')

                    log_info = {
                        'file_path': str(log_file),
                        'market': market_dir.name,
                        'date': date_str,
                        'decision_id': decision_id,
                        'timestamp': timestamp,
                        'file_size': log_file.stat().st_size
                    }
                    logs.append(log_info)

                except Exception as e:
                    print(f"Warning: Error processing {log_file}: {e}")
                    continue

    except Exception as e:
        print(f"Error scanning decision logs: {e}")

    # Sort by timestamp (newest first)
    logs.sort(key=lambda x: x['timestamp'], reverse=True)
    return logs

async def interactive_manual_learning():
    """Interactive manual learning session"""
    print("\n" + "="*60)
    print("      Interactive Manual Learning Session")
    print("="*60 + "\n")

    try:
        # List available decision logs
        print("[STEP 1] Scanning available decision logs...")
        logs = list_available_decision_logs()

        if not logs:
            print("[ERROR] No decision logs found!")
            return

        print(f"[SUCCESS] Found {len(logs)} decision logs")

        # Display logs for selection
        print("\nAvailable Decision Logs:")
        print("-" * 80)
        for i, log in enumerate(logs[:20]):  # Show first 20
            print(f"{i+1:2d}. {log['market']:15s} | {log['date']:10s} | {log['decision_id']}")

        if len(logs) > 20:
            print(f"... and {len(logs) - 20} more logs")

        # Get user selection
        while True:
            try:
                selection = input(f"\nSelect a decision log (1-{min(20, len(logs))}): ")
                index = int(selection) - 1
                if 0 <= index < min(20, len(logs)):
                    selected_log = logs[index]
                    break
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        # Get PnL value
        while True:
            try:
                pnl_input = input("Enter the realized PnL value: ")
                pnl_value = float(pnl_input)
                break
            except ValueError:
                print("Please enter a valid number.")

        # Get optional user notes
        user_notes = input("Enter any notes (optional): ").strip()

        # Execute manual learning
        print(f"\n[STEP 2] Executing manual learning...")
        result = await manual_learning(
            selected_log['file_path'],
            pnl_value,
            user_notes
        )

        if result['success']:
            print("\n[SUCCESS] Interactive manual learning completed!")
        else:
            print(f"\n[ERROR] Learning failed: {result.get('error', 'Unknown error')}")

    except KeyboardInterrupt:
        print("\n\n[INFO] Manual learning session cancelled by user.")
    except Exception as e:
        print(f"\n[ERROR] Interactive session failed: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Trading Agents Learning Engine")
    parser.add_argument('--mode', choices=['auto', 'manual', 'interactive'],
                       default='auto', help='Learning mode')
    parser.add_argument('--decision-log', type=str,
                       help='Path to decision log file (for manual mode)')
    parser.add_argument('--pnl', type=float,
                       help='PnL value (for manual mode)')
    parser.add_argument('--notes', type=str, default='',
                       help='User notes (for manual mode)')
    parser.add_argument('--list-logs', action='store_true',
                       help='List available decision logs')

    args = parser.parse_args()

    if args.list_logs:
        print("Available Decision Logs:")
        print("=" * 80)
        logs = list_available_decision_logs()
        for log in logs:
            print(f"{log['market']:15s} | {log['date']:10s} | {log['decision_id']} | {log['file_path']}")
        print(f"\nTotal: {len(logs)} logs found")

    elif args.mode == 'auto':
        asyncio.run(main())

    elif args.mode == 'manual':
        if not args.decision_log or args.pnl is None:
            print("Error: Manual mode requires --decision-log and --pnl arguments")
            sys.exit(1)

        result = asyncio.run(manual_learning(args.decision_log, args.pnl, args.notes))
        if not result['success']:
            sys.exit(1)

    elif args.mode == 'interactive':
        asyncio.run(interactive_manual_learning())
