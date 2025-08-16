#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test chat trader with open orders functionality
"""

import os
import sys
from datetime import datetime

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from tradingagents.agents.trader.chat_trader import create_chat_trader

# Set output encoding for Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())

# Load environment variables
load_dotenv()

def test_trader_with_orders():
    """Test chat trader with open orders feature"""
    print("=" * 60)
    print("Testing Chat Trader with Open Orders")
    print("=" * 60)
    
    # Initialize LLM
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ Please set OPENAI_API_KEY environment variable")
        return
    
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.0,
        api_key=api_key,
        base_url=os.getenv('TRADINGAGENTS_BACKEND_URL', 'https://api.openai.com/v1')
    )
    
    # Create chat trader
    chat_trader = create_chat_trader(llm)
    
    # Test messages focused on orders
    test_messages = [
        {
            "role": "user",
            "content": "请帮我分析一下我当前的交易状况，包括持仓、挂单和近期交易历史。有什么需要注意的吗？"
        }
    ]
    
    print("\n[TEST] Sending message to trader...")
    print(f"User: {test_messages[0]['content']}")
    print("\n" + "-" * 40)
    
    try:
        response = chat_trader(test_messages)
        print("Trader Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)
    except Exception as e:
        print(f"❌ Trader response failed: {str(e)}")
    
    # Test with specific order-related question
    print("\n" + "=" * 60)
    print("Testing Order-Specific Questions")
    print("=" * 60)
    
    order_messages = [
        {
            "role": "user",
            "content": "我目前有哪些挂单？需要调整吗？如果没有挂单，你建议我设置什么样的挂单策略？"
        }
    ]
    
    print(f"\nUser: {order_messages[0]['content']}")
    print("\n" + "-" * 40)
    
    try:
        response = chat_trader(order_messages)
        print("Trader Response:")
        print("-" * 40)
        print(response)
        print("-" * 40)
    except Exception as e:
        print(f"❌ Trader response failed: {str(e)}")

def main():
    """Main test function"""
    print("🚀 Chat Trader with Orders Test Starting")
    print(f"🕒 Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    test_trader_with_orders()
    
    print("\n" + "=" * 60)
    print("🎉 Test completed!")
    print("=" * 60)

if __name__ == "__main__":
    main()