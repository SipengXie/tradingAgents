#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Manual Learning CLI Tool

A command-line interface for the manual learning system.
Provides easy access to decision logs and manual learning functionality.
"""

import asyncio
import sys
import argparse
from pathlib import Path
from datetime import datetime
import json

# Add project root to sys.path
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from scripts.learning_engine import (
    list_available_decision_logs,
    manual_learning,
    interactive_manual_learning
)

def print_banner():
    """Print CLI banner"""
    print("\n" + "="*70)
    print("🧠 TRADING AGENTS - MANUAL LEARNING CLI")
    print("="*70)
    print("📚 Learn from past decisions with manual PnL input")
    print("🎯 Targeted learning for specific trading scenarios")
    print("="*70 + "\n")

def list_logs_command():
    """List all available decision logs"""
    print("📋 Scanning for decision logs...")
    logs = list_available_decision_logs()
    
    if not logs:
        print("❌ No decision logs found!")
        return
    
    print(f"✅ Found {len(logs)} decision logs\n")
    
    # Group by market
    markets = {}
    for log in logs:
        market = log['market']
        if market not in markets:
            markets[market] = []
        markets[market].append(log)
    
    # Display grouped logs
    for market, market_logs in markets.items():
        print(f"📊 {market} ({len(market_logs)} logs)")
        print("-" * 60)
        
        for log in market_logs[:10]:  # Show first 10 per market
            date = log['date']
            decision_id = log['decision_id'][:20] + "..." if len(log['decision_id']) > 20 else log['decision_id']
            size_kb = log['file_size'] // 1024
            print(f"  📅 {date} | 🆔 {decision_id:<23} | 📁 {size_kb:3d}KB")
        
        if len(market_logs) > 10:
            print(f"  ... and {len(market_logs) - 10} more logs")
        print()

def search_logs_command(query: str):
    """Search decision logs by query"""
    print(f"🔍 Searching for logs matching: '{query}'")
    logs = list_available_decision_logs()
    
    # Filter logs based on query
    matching_logs = []
    query_lower = query.lower()
    
    for log in logs:
        if (query_lower in log['market'].lower() or 
            query_lower in log['decision_id'].lower() or 
            query_lower in log['date'].lower()):
            matching_logs.append(log)
    
    if not matching_logs:
        print("❌ No matching logs found!")
        return
    
    print(f"✅ Found {len(matching_logs)} matching logs\n")
    
    for i, log in enumerate(matching_logs[:20], 1):
        print(f"{i:2d}. 📊 {log['market']:15s} | 📅 {log['date']:10s} | 🆔 {log['decision_id']}")
        print(f"    📁 {log['file_path']}")
        print()

async def learn_command(decision_log: str, pnl: float, notes: str = ""):
    """Execute manual learning"""
    print(f"🎓 Starting manual learning session...")
    print(f"📄 Decision log: {Path(decision_log).name}")
    print(f"💰 PnL: {pnl:+.4f}")
    if notes:
        print(f"📝 Notes: {notes}")
    print()
    
    result = await manual_learning(decision_log, pnl, notes)
    
    if result['success']:
        print("✅ Manual learning completed successfully!")
        
        # Save result to file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result_file = project_root / f"eval_results/manual_learning_{timestamp}.json"
        
        with open(result_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Results saved to: {result_file}")
        
        # Display summary
        print("\n📊 Learning Summary:")
        print(f"  🆔 Decision ID: {result['decision_id']}")
        print(f"  💰 PnL: {result['input_pnl']:+.4f}")
        print(f"  🕒 Timestamp: {result['timestamp']}")
        print(f"  🧠 Components learned: {len(result['reflections'])}")
        
    else:
        print(f"❌ Learning failed: {result.get('error', 'Unknown error')}")
        return False
    
    return True

def show_log_detail(log_path: str):
    """Show detailed information about a decision log"""
    try:
        log_file = Path(log_path)
        if not log_file.exists():
            print(f"❌ Log file not found: {log_path}")
            return
        
        with open(log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)
        
        # Handle different log formats
        if isinstance(log_data, dict):
            if 'decision_id' in log_data:
                decision_data = log_data
            else:
                decision_data = next(iter(log_data.values())) if log_data else {}
        else:
            print("❌ Invalid log format")
            return
        
        print(f"📄 Decision Log Details")
        print("=" * 50)
        print(f"🆔 Decision ID: {decision_data.get('decision_id', 'Unknown')}")
        print(f"🕒 Timestamp: {decision_data.get('timestamp', 'Unknown')}")
        print(f"📁 File: {log_file.name}")
        print(f"📊 Size: {log_file.stat().st_size // 1024} KB")
        
        # Show market analysis if available
        market_analysis = decision_data.get('market_analysis', {})
        if isinstance(market_analysis, dict):
            print(f"\n📈 Market Analysis:")
            for key, value in market_analysis.items():
                if isinstance(value, (str, int, float)):
                    print(f"  {key}: {value}")
        
        # Show trading decision if available
        trading_decision = decision_data.get('trading_decision', {})
        if isinstance(trading_decision, dict):
            print(f"\n💼 Trading Decision:")
            for key, value in trading_decision.items():
                if isinstance(value, (str, int, float)):
                    print(f"  {key}: {value}")
        
    except Exception as e:
        print(f"❌ Error reading log: {e}")

async def main():
    """Main CLI function"""
    parser = argparse.ArgumentParser(
        description="Manual Learning CLI for Trading Agents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python manual_learning_cli.py list                           # List all decision logs
  python manual_learning_cli.py search BTC                     # Search for BTC-related logs
  python manual_learning_cli.py learn path/to/log.json 5.25    # Learn with +5.25 PnL
  python manual_learning_cli.py detail path/to/log.json        # Show log details
  python manual_learning_cli.py interactive                    # Interactive mode
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    subparsers.add_parser('list', help='List all available decision logs')
    
    # Search command
    search_parser = subparsers.add_parser('search', help='Search decision logs')
    search_parser.add_argument('query', help='Search query')
    
    # Learn command
    learn_parser = subparsers.add_parser('learn', help='Execute manual learning')
    learn_parser.add_argument('decision_log', help='Path to decision log file')
    learn_parser.add_argument('pnl', type=float, help='Realized PnL value')
    learn_parser.add_argument('--notes', default='', help='Optional notes')
    
    # Detail command
    detail_parser = subparsers.add_parser('detail', help='Show decision log details')
    detail_parser.add_argument('log_path', help='Path to decision log file')
    
    # Interactive command
    subparsers.add_parser('interactive', help='Interactive manual learning session')
    
    args = parser.parse_args()
    
    if not args.command:
        print_banner()
        parser.print_help()
        return
    
    print_banner()
    
    try:
        if args.command == 'list':
            list_logs_command()
        
        elif args.command == 'search':
            search_logs_command(args.query)
        
        elif args.command == 'learn':
            success = await learn_command(args.decision_log, args.pnl, args.notes)
            if not success:
                sys.exit(1)
        
        elif args.command == 'detail':
            show_log_detail(args.log_path)
        
        elif args.command == 'interactive':
            await interactive_manual_learning()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())
