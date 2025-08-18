#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Learning Automation Manager for Trading Agents

This module provides a class to manage the learning process from real-world trades.
"""

import asyncio
import json
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import List, Dict, Any

from dotenv import load_dotenv

# Ensure the project root is in the Python path
project_root = Path(__file__).resolve().parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.agents.utils.paradex_tools import ParadexDataManager
from tradingagents.agents.utils.memory import FinancialSituationMemory
from tradingagents.default_config import DEFAULT_CONFIG

class LearningManager:
    """Manages fetching trades, running reflections, and retrieving learned reports."""

    def __init__(self):
        """Initializes the LearningManager."""
        self.project_root = Path(__file__).resolve().parent.parent.parent
        self.processed_fills_log = self.project_root / "eval_results/processed_fills.log"
        self.decision_logs_dir = self.project_root / "eval_results"
        self.paradex_manager = ParadexDataManager()
        self.trading_agents_graph = TradingAgentsGraph()
        load_dotenv(self.project_root / ".env")

    def _load_processed_fills(self) -> set:
        """Reads the processed fills log and returns a set of fill IDs."""
        if not self.processed_fills_log.exists():
            return set()
        with open(self.processed_fills_log, 'r') as f:
            return {line.strip() for line in f if line.strip()}

    def _save_processed_fill(self, fill_id: str):
        """Appends a new fill ID to the processed fills log."""
        with open(self.processed_fills_log, 'a') as f:
            f.write(f"{fill_id}\n")

    def _find_decision_log(self, fill_timestamp_ms: int, market: str) -> Path | None:
        """Finds the decision log file corresponding to a fill."""
        sanitized_market = market.replace("-PERP", "")
        fill_dt = datetime.fromtimestamp(fill_timestamp_ms / 1000)
        for i in range(2):
            search_date = (fill_dt - timedelta(days=i)).date()
            log_dir = self.decision_logs_dir / sanitized_market / "TradingAgentsStrategy_logs"
            log_file = log_dir / f"full_states_log_{search_date}.json"
            if log_file.exists():
                return log_file
        return None

    def get_unlearned_trades(self) -> List[Dict[str, Any]]:
        """Fetches all trades and returns the ones that have not been processed yet."""
        print("[INFO] Fetching trading history from Paradex...")
        history_data = self.paradex_manager.get_trading_history(limit=100, days=30)
        if not history_data.get("success"):
            print(f"[ERROR] Failed to fetch trading history: {history_data.get('error')}")
            return []

        all_fills = history_data.get("recent_trades", [])
        if not all_fills:
             all_fills = history_data.get("analysis",{}).get("recent_trades",[])

        processed_fills = self._load_processed_fills()
        new_fills = [f for f in all_fills if f['id'] not in processed_fills]
        return new_fills

    def learn_from_all_new_trades(self) -> Dict[str, Any]:
        """Processes all new, unlearned trades and returns a summary."""
        new_fills = self.get_unlearned_trades()
        if not new_fills:
            return {"message": "No new trades to learn from.", "learned_count": 0}

        print(f"[INFO] Found {len(new_fills)} new fills to process.")
        learned_count = 0
        for fill in new_fills:
            pnl = float(fill.get('realized_pnl', 0.0))
            if pnl == 0.0:
                self._save_processed_fill(fill['id'])
                continue

            log_path = self._find_decision_log(fill['created_at'], fill['market'])
            if not log_path:
                self._save_processed_fill(fill['id'])
                continue

            with open(log_path, 'r', encoding='utf-8') as f:
                loaded_json = json.load(f)
            
            if loaded_json.get('decision_id'):
                historical_state = loaded_json
            else:
                historical_state = next(iter(loaded_json.values()))

            print(f"[INFO] Learning from Fill ID: {fill['id']} with PnL: {pnl:.4f}")
            self.trading_agents_graph.reflect_on_past_decision(historical_state, pnl)
            self._save_processed_fill(fill['id'])
            learned_count += 1
        
        return {"message": f"Successfully learned from {learned_count} trades.", "learned_count": learned_count}

    def get_all_learned_reports(self) -> Dict[str, List[Dict[str, Any]]]:
        """Retrieves all learned experiences from the memory database."""
        memory_components = [
            "bull_memory", "bear_memory", "trader_memory",
            "invest_judge_memory", "risk_manager_memory",
        ]
        all_reports = {}
        config = DEFAULT_CONFIG
        config["project_dir"] = str(self.project_root)

        for memory_name in memory_components:
            try:
                memory = FinancialSituationMemory(memory_name, config)
                collection = memory.situation_collection
                results = collection.get(include=["metadatas", "documents"])
                if not results or not results['ids']:
                    all_reports[memory_name] = []
                    continue
                
                reports = []
                for i in range(len(results['ids'])):
                    reports.append({
                        "situation": results['documents'][i],
                        "reflection": results['metadatas'][i].get('recommendation', 'N/A')
                    })
                all_reports[memory_name] = reports
            except Exception as e:
                print(f"[ERROR] Failed to read memory for '{memory_name}': {e}")
                all_reports[memory_name] = []
        return all_reports

async def main_script_runner():
    """Function to run learning process from script, for testing."""
    manager = LearningManager()
    summary = await asyncio.to_thread(manager.learn_from_all_new_trades)
    print(summary["message"])

if __name__ == "__main__":
    # This allows running this file directly for testing the LearningManager
    asyncio.run(main_script_runner())
