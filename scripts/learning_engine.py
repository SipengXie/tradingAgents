#!/usr/bin/env python3
# -*- coding: utf-8 -*"""
"""
Trading Agents Learning Engine

This script runs a learning cycle based on real-world trade data from Paradex.
It fetches recent trades, matches them with the agent's past decisions,
and triggers a reflection process to update the agent's memory with lessons learned.

"""

import asyncio
import json
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta

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

if __name__ == "__main__":
    asyncio.run(main())
