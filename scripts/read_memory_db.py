#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Read Trading Agents Memory Script

This script connects to the ChromaDB memory database and prints out the 
learned experiences (situations and recommendations) for each agent component.
"""

import os
import sys
from pathlib import Path

# Add project root to sys.path to allow imports from tradingagents
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))

from tradingagents.agents.utils.memory import FinancialSituationMemory
from tradingagents.default_config import DEFAULT_CONFIG

def read_and_print_memory(memory_name: str, config: dict):
    """Initializes a memory collection and prints its contents."""
    print("\n" + "="*60)
    print(f"      🧠 Reading Memory For: {memory_name.upper()} 🧠")
    print("="*60 + "\n")

    try:
        memory = FinancialSituationMemory(memory_name, config)
        # Use the underlying collection object to get all items
        collection = memory.situation_collection
        
        # ChromaDB's get() method can retrieve all items without a query
        results = collection.get(include=["metadatas", "documents"])
        
        if not results or not results['ids']:
            print("  -> This memory collection is empty.")
            return

        count = len(results['ids'])
        print(f"  -> Found {count} learned experience(s) in this collection.\n")

        # Iterate through the results and print them
        for i in range(count):
            situation = results['documents'][i]
            recommendation = results['metadatas'][i].get('recommendation', 'N/A')
            
            print("-"*50)
            print(f"  MEMORY #{i + 1}")
            print("-"*50)
            print("\n[SITUATION] \n" + "-"*11)
            print(situation)
            print("\n[LEARNED RECOMMENDATION / REFLECTION] \n" + "-"*38)
            print(recommendation)
            print("\n")

    except Exception as e:
        print(f"[ERROR] Failed to read memory for '{memory_name}'.")
        print(f"  Reason: {e}")

def main():
    """Main function to read all memory collections."""
    # List of all memory components used in the project
    memory_components = [
        "bull_memory",
        "bear_memory",
        "trader_memory",
        "invest_judge_memory",
        "risk_manager_memory",
    ]

    # Use the project's default config
    # We need to provide a project_dir to the config so it knows where to find memory_db
    config = DEFAULT_CONFIG
    config["project_dir"] = str(project_root)

    for memory_name in memory_components:
        read_and_print_memory(memory_name, config)

if __name__ == "__main__":
    main()
