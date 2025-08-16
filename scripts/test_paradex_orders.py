#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script for Paradex open orders functionality
"""

import os
import sys
from datetime import datetime

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from tradingagents.agents.utils.paradex_tools import (
    get_paradex_manager,
    format_open_orders_for_trader,
    format_positions_for_trader,
    format_trading_history_for_trader
)

# Set output encoding for Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# Load environment variables
load_dotenv()

def test_open_orders():
    """Test fetching and displaying open orders"""
    print("=" * 60)
    print("Testing Paradex Open Orders Functionality")
    print("=" * 60)
    
    manager = get_paradex_manager()
    
    # Test fetching open orders for all markets
    print("\n[TEST] Fetching all open orders...")
    orders_data = manager.get_open_orders()
    
    if orders_data.get("success"):
        print("✅ Open orders fetched successfully")
        
        # Display analysis
        analysis = orders_data.get("analysis", {})
        total_orders = orders_data.get("total_orders", 0)
        
        if total_orders > 0:
            print(f"\n📊 Order Summary:")
            print(f"   - Total Orders: {total_orders}")
            print(f"   - Buy Orders: {analysis.get('total_buy_orders', 0)}")
            print(f"   - Sell Orders: {analysis.get('total_sell_orders', 0)}")
            print(f"   - Total Notional: {analysis.get('total_notional_value', 0):,.2f} USDC")
            print(f"   - Unique Markets: {analysis.get('unique_markets', 0)}")
            
            # Display market breakdown
            market_breakdown = analysis.get('market_breakdown', {})
            if market_breakdown:
                print(f"\n📈 Market Breakdown:")
                for market, stats in market_breakdown.items():
                    print(f"   {market}:")
                    print(f"     - Orders: {stats['orders']}")
                    print(f"     - Buy/Sell: {stats['buy_orders']}/{stats['sell_orders']}")
                    print(f"     - Total Size: {stats['total_size']:.4f}")
                    
                    order_types = stats.get('order_types', {})
                    if order_types:
                        print(f"     - Order Types: {', '.join([f'{t}: {c}' for t, c in order_types.items()])}")
        else:
            print("📭 No open orders found")
            
        # Test formatted output for trader
        print("\n" + "-" * 40)
        print("Formatted Output for Trader:")
        print("-" * 40)
        formatted_output = format_open_orders_for_trader(orders_data)
        print(formatted_output)
        
    else:
        print(f"❌ Failed to fetch open orders: {orders_data.get('error', 'Unknown error')}")
    
    # Test fetching orders for specific market (if applicable)
    test_market = "BTC-USD-PERP"
    print(f"\n[TEST] Fetching open orders for {test_market}...")
    market_orders = manager.get_open_orders(market=test_market)
    
    if market_orders.get("success"):
        total_market_orders = market_orders.get("total_orders", 0)
        print(f"✅ Found {total_market_orders} open orders for {test_market}")
    else:
        print(f"❌ Failed to fetch orders for {test_market}: {market_orders.get('error', 'Unknown error')}")

def test_complete_portfolio():
    """Test complete portfolio overview including new orders feature"""
    print("\n" + "=" * 60)
    print("Complete Portfolio Overview Test")
    print("=" * 60)
    
    manager = get_paradex_manager()
    
    # Get all portfolio data
    print("\n📊 Fetching complete portfolio data...")
    
    # 1. Positions
    positions = manager.get_positions_summary()
    print("\n1️⃣ Positions:")
    if positions.get("success"):
        print(f"   ✅ {positions.get('total_positions', 0)} active positions")
        print(f"   💰 Unrealized P&L: {positions.get('total_unrealized_pnl', 0):+.2f} USDC")
    else:
        print(f"   ❌ Error: {positions.get('error', 'Unknown')}")
    
    # 2. Open Orders
    orders = manager.get_open_orders()
    print("\n2️⃣ Open Orders:")
    if orders.get("success"):
        analysis = orders.get("analysis", {})
        print(f"   ✅ {orders.get('total_orders', 0)} open orders")
        if orders.get("total_orders", 0) > 0:
            print(f"   📈 Buy/Sell: {analysis.get('total_buy_orders', 0)}/{analysis.get('total_sell_orders', 0)}")
            print(f"   💵 Notional Value: {analysis.get('total_notional_value', 0):,.2f} USDC")
    else:
        print(f"   ❌ Error: {orders.get('error', 'Unknown')}")
    
    # 3. Trading History
    history = manager.get_trading_history(limit=20, days=7)
    print("\n3️⃣ Trading History (Last 7 days):")
    if history.get("success"):
        analysis = history.get("analysis", {})
        print(f"   ✅ {analysis.get('total_trades', 0)} trades executed")
        print(f"   💰 Realized P&L: {analysis.get('total_realized_pnl', 0):+.2f} USDC")
        print(f"   💸 Total Fees: {analysis.get('total_fees', 0):.2f} USDC")
    else:
        print(f"   ❌ Error: {history.get('error', 'Unknown')}")
    
    # 4. Risk Metrics
    risk_metrics = manager.get_risk_metrics()
    print("\n4️⃣ Risk Metrics:")
    if not risk_metrics.get("error"):
        concentration = risk_metrics.get("portfolio_concentration", {})
        if concentration:
            print(f"   ✅ Total Exposure: {concentration.get('total_exposure_usdc', 0):,.2f} USDC")
            print(f"   📊 Max Concentration: {concentration.get('max_concentration', 0):.1f}%")
    else:
        print(f"   ❌ Error: {risk_metrics.get('error', 'Unknown')}")

def main():
    """Main test function"""
    print("🚀 Paradex Open Orders Test Starting")
    print(f"🕒 Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Run tests
    test_open_orders()
    test_complete_portfolio()
    
    print("\n" + "=" * 60)
    print("🎉 All tests completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()