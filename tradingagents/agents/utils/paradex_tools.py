# -*- coding: utf-8 -*-
"""
Paradex 数据获取工具模块
提供交易员智能体访问 Paradex 仓位和历史交易数据的功能
"""

import os
import asyncio
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 延迟导入 paradex_py 以避免启动时的依赖问题
_paradex_py_available = False
try:
    from paradex_py import Paradex
    _paradex_py_available = True
except ImportError as e:
    print(f"[警告] Paradex SDK 不可用: {str(e)}")
    print("[信息] Paradex 功能将被禁用，交易员将在没有实时数据的情况下运行")
    _paradex_py_available = False


class ParadexDataManager:
    """Paradex 数据管理器"""
    
    def __init__(self):
        self.client = None
        self._initialized = False
        
    def _initialize_client(self):
        """初始化 Paradex 客户端"""
        if self._initialized:
            return
            
        if not _paradex_py_available:
            print("[警告] Paradex SDK 不可用，无法初始化客户端")
            return
            
        try:
            # 确保当前线程有事件循环
            try:
                loop = asyncio.get_running_loop()
            except RuntimeError:  # 'RuntimeError: There is no current event loop...'
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
            
            l1_address = os.getenv('PARADEX_ADDR')
            l1_private_key = os.getenv('PARADEX_KEY')
            
            if not l1_address or not l1_private_key:
                raise ValueError("PARADEX_ADDR 和 PARADEX_KEY 环境变量未设置")
                
            self.client = Paradex(
                env="prod",
                l1_address=l1_address,
                l1_private_key=l1_private_key
            )
            self._initialized = True
            
        except Exception as e:
            print(f"[警告] Paradex 客户端初始化失败: {str(e)}")
            self.client = None

    def get_positions_summary(self) -> Dict[str, Any]:
        """获取持仓摘要信息"""
        if not _paradex_py_available:
            return {"error": "Paradex SDK 不可用"}
            
        try:
            self._initialize_client()
            if not self.client:
                return {"error": "Paradex 客户端未初始化"}
                
            positions_response = self.client.api_client.fetch_positions()
            
            if not isinstance(positions_response, dict) or 'results' not in positions_response:
                return {"error": "获取持仓数据格式错误"}
                
            positions = positions_response['results']
            
            # 过滤出有实际持仓的品种
            active_positions = []
            total_unrealized_pnl = 0.0
            
            for pos in positions:
                size = float(pos.get('size', 0))
                if size != 0:  # 只包含非零持仓
                    active_positions.append(pos)
                    pnl = float(pos.get('unrealized_pnl', 0))
                    total_unrealized_pnl += pnl
            
            return {
                "success": True,
                "total_positions": len(active_positions),
                "total_unrealized_pnl": total_unrealized_pnl,
                "positions": active_positions,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
        except Exception as e:
            return {"error": f"获取持仓信息失败: {str(e)}"}

    def get_open_orders(self, market: Optional[str] = None) -> Dict[str, Any]:
        """获取当前挂单信息
        
        Args:
            market: 可选的市场符号（如 'BTC-USD-PERP'），不指定则返回所有市场的挂单
            
        Returns:
            包含挂单信息的字典
        """
        if not _paradex_py_available:
            return {"error": "Paradex SDK 不可用"}
            
        try:
            self._initialize_client()
            if not self.client:
                return {"error": "Paradex 客户端未初始化"}
                
            # 构建查询参数
            params = {}
            if market:
                params['market'] = market
                
            # 获取挂单数据
            orders_response = self.client.api_client.fetch_orders(params=params)
            
            if not isinstance(orders_response, dict) or 'results' not in orders_response:
                return {"error": "获取挂单数据格式错误"}
                
            orders = orders_response['results']
            
            # 过滤出活跃的挂单（未成交、未取消的订单）
            active_orders = []
            for order in orders:
                status = order.get('status', '').upper()
                # Paradex 的订单状态通常包括: OPEN, FILLED, CANCELLED, EXPIRED
                if status in ['OPEN', 'PENDING', 'PARTIAL']:
                    active_orders.append(order)
            
            # 分析挂单数据
            analysis = self._analyze_open_orders(active_orders)
            
            return {
                "success": True,
                "total_orders": len(active_orders),
                "analysis": analysis,
                "orders": active_orders,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
        except Exception as e:
            return {"error": f"获取挂单信息失败: {str(e)}"}
    
    def _analyze_open_orders(self, orders: List[Dict]) -> Dict[str, Any]:
        """分析挂单数据"""
        if not orders:
            return {"message": "当前无挂单"}
            
        # 按市场统计
        market_stats = {}
        total_buy_orders = 0
        total_sell_orders = 0
        total_notional = 0.0
        
        for order in orders:
            market = order.get('market', 'Unknown')
            side = order.get('side', '').upper()
            size = float(order.get('size', 0))
            price = float(order.get('price', 0))
            order_type = order.get('type', 'Unknown')
            
            if market not in market_stats:
                market_stats[market] = {
                    'orders': 0,
                    'buy_orders': 0,
                    'sell_orders': 0,
                    'total_size': 0.0,
                    'order_types': {}
                }
            
            market_stats[market]['orders'] += 1
            market_stats[market]['total_size'] += size
            
            if side == 'BUY':
                total_buy_orders += 1
                market_stats[market]['buy_orders'] += 1
            else:
                total_sell_orders += 1
                market_stats[market]['sell_orders'] += 1
                
            # 统计订单类型
            if order_type not in market_stats[market]['order_types']:
                market_stats[market]['order_types'][order_type] = 0
            market_stats[market]['order_types'][order_type] += 1
            
            # 计算名义价值
            total_notional += size * price
        
        return {
            "total_buy_orders": total_buy_orders,
            "total_sell_orders": total_sell_orders,
            "total_notional_value": total_notional,
            "market_breakdown": market_stats,
            "unique_markets": len(market_stats)
        }

    def get_trading_history(self, limit: int = 20, days: int = 30) -> Dict[str, Any]:
        """获取交易历史摘要"""
        if not _paradex_py_available:
            return {"error": "Paradex SDK 不可用"}
            
        try:
            self._initialize_client()
            if not self.client:
                return {"error": "Paradex 客户端未初始化"}
                
            # 计算时间范围
            end_time = int(datetime.now().timestamp() * 1000)
            start_time = int((datetime.now() - timedelta(days=days)).timestamp() * 1000)
            
            params = {
                "page_size": limit,
                "start_at": start_time,
                "end_at": end_time
            }
            
            fills_response = self.client.api_client.fetch_fills(params=params)
            
            if not isinstance(fills_response, dict) or 'results' not in fills_response:
                return {"error": "获取交易历史数据格式错误"}
                
            fills = fills_response['results']
            
            # 分析交易数据
            analysis = self._analyze_trading_history(fills)
            
            return {
                "success": True,
                "total_trades": len(fills),
                "analysis": analysis,
                "recent_trades": fills[:5],  # 最近5笔交易
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
        except Exception as e:
            return {"error": f"获取交易历史失败: {str(e)}"}

    def _analyze_trading_history(self, fills: List[Dict]) -> Dict[str, Any]:
        """分析交易历史数据"""
        if not fills:
            return {"message": "暂无交易记录"}
            
        # 基础统计
        total_trades = len(fills)
        buy_trades = sum(1 for fill in fills if fill.get('side', '').lower() == 'buy')
        sell_trades = total_trades - buy_trades
        
        # 按交易对统计
        symbol_stats = {}
        total_realized_pnl = 0.0
        total_fees = 0.0
        
        for fill in fills:
            symbol = fill.get('market', 'Unknown')
            side = fill.get('side', 'Unknown')
            size = float(fill.get('size', 0))
            price = float(fill.get('price', 0))
            fee = float(fill.get('fee', 0))
            pnl = fill.get('realized_pnl')
            
            if symbol not in symbol_stats:
                symbol_stats[symbol] = {
                    'trades': 0,
                    'volume': 0.0,
                    'buy_trades': 0,
                    'sell_trades': 0
                }
            
            symbol_stats[symbol]['trades'] += 1
            symbol_stats[symbol]['volume'] += size
            
            if side.lower() == 'buy':
                symbol_stats[symbol]['buy_trades'] += 1
            else:
                symbol_stats[symbol]['sell_trades'] += 1
                
            total_fees += fee
            if pnl and pnl != 'N/A':
                try:
                    total_realized_pnl += float(pnl)
                except:
                    pass
        
        # 获取最活跃的交易对
        most_active = max(symbol_stats.items(), key=lambda x: x[1]['trades']) if symbol_stats else None
        
        return {
            "total_trades": total_trades,
            "buy_trades": buy_trades,
            "sell_trades": sell_trades,
            "total_realized_pnl": total_realized_pnl,
            "total_fees": total_fees,
            "unique_symbols": len(symbol_stats),
            "most_active_symbol": most_active[0] if most_active else None,
            "symbol_breakdown": symbol_stats
        }

    def get_portfolio_overview(self) -> Dict[str, Any]:
        """获取投资组合概览"""
        try:
            positions = self.get_positions_summary()
            history = self.get_trading_history(limit=50, days=7)  # 最近一周
            
            if positions.get("error") and history.get("error"):
                return {"error": "无法获取投资组合数据"}
                
            overview = {
                "success": True,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "positions_summary": positions,
                "trading_summary": history
            }
            
            # 生成投资组合洞察
            insights = self._generate_portfolio_insights(positions, history)
            overview["insights"] = insights
            
            return overview
            
        except Exception as e:
            return {"error": f"获取投资组合概览失败: {str(e)}"}

    def _generate_portfolio_insights(self, positions: Dict, history: Dict) -> List[str]:
        """生成投资组合洞察"""
        insights = []
        
        try:
            # 持仓洞察
            if positions.get("success"):
                pos_count = positions.get("total_positions", 0)
                total_pnl = positions.get("total_unrealized_pnl", 0)
                
                if pos_count == 0:
                    insights.append("📊 当前无持仓，处于空仓状态")
                else:
                    insights.append(f"📊 当前持有 {pos_count} 个品种的仓位")
                    if total_pnl > 0:
                        insights.append(f"💰 总未实现盈亏: +{total_pnl:.2f} USDC (盈利)")
                    elif total_pnl < 0:
                        insights.append(f"📉 总未实现盈亏: {total_pnl:.2f} USDC (亏损)")
            
            # 交易活动洞察
            if history.get("success"):
                analysis = history.get("analysis", {})
                total_trades = analysis.get("total_trades", 0)
                realized_pnl = analysis.get("total_realized_pnl", 0)
                most_active = analysis.get("most_active_symbol")
                
                if total_trades > 0:
                    insights.append(f"📈 最近交易活跃度: {total_trades} 笔交易")
                    if realized_pnl > 0:
                        insights.append(f"✅ 已实现收益: +{realized_pnl:.2f} USDC")
                    elif realized_pnl < 0:
                        insights.append(f"❌ 已实现亏损: {realized_pnl:.2f} USDC")
                    
                    if most_active:
                        insights.append(f"🎯 最活跃交易品种: {most_active}")
                else:
                    insights.append("📭 最近无交易记录")
                    
        except Exception as e:
            insights.append(f"⚠️ 洞察生成失败: {str(e)}")
            
        return insights

    def get_risk_metrics(self) -> Dict[str, Any]:
        """获取风险指标"""
        try:
            positions = self.get_positions_summary()
            history = self.get_trading_history(limit=100, days=30)
            
            risk_metrics = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "portfolio_concentration": {},
                "trading_frequency": {},
                "pnl_volatility": {}
            }
            
            # 分析持仓集中度
            if positions.get("success") and positions.get("positions"):
                active_positions = positions["positions"]
                if active_positions:
                    total_exposure = sum(abs(float(pos.get('size', 0)) * float(pos.get('mark_price', 0))) 
                                       for pos in active_positions)
                    
                    if total_exposure > 0:
                        concentrations = {}
                        for pos in active_positions:
                            symbol = pos.get('market', 'Unknown')
                            exposure = abs(float(pos.get('size', 0)) * float(pos.get('mark_price', 0)))
                            concentrations[symbol] = (exposure / total_exposure) * 100
                        
                        risk_metrics["portfolio_concentration"] = {
                            "total_exposure_usdc": total_exposure,
                            "concentrations": concentrations,
                            "max_concentration": max(concentrations.values()) if concentrations else 0
                        }
            
            # 分析交易频率
            if history.get("success"):
                analysis = history["analysis"]
                risk_metrics["trading_frequency"] = {
                    "trades_per_week": analysis.get("total_trades", 0),
                    "avg_trade_size": "需要更多数据计算",
                    "trading_pairs": analysis.get("unique_symbols", 0)
                }
            
            return risk_metrics
            
        except Exception as e:
            return {"error": f"获取风险指标失败: {str(e)}"}


# 全局实例
_paradex_manager = None

def get_paradex_manager() -> ParadexDataManager:
    """获取 Paradex 数据管理器实例"""
    global _paradex_manager
    if _paradex_manager is None:
        _paradex_manager = ParadexDataManager()
    return _paradex_manager


def format_positions_for_trader(positions_data: Dict[str, Any]) -> str:
    """为交易员智能体格式化持仓数据"""
    if positions_data.get("error"):
        return f"⚠️ Paradex 持仓数据获取失败: {positions_data['error']}"
    
    if not positions_data.get("success"):
        return "⚠️ 无法获取 Paradex 持仓数据"
    
    result = "=== 📊 Paradex 实时持仓状况 ===\n"
    
    total_positions = positions_data.get("total_positions", 0)
    total_pnl = positions_data.get("total_unrealized_pnl", 0)
    
    if total_positions == 0:
        result += "📭 当前无持仓，账户处于空仓状态\n"
    else:
        result += f"📈 持仓品种数量: {total_positions}\n"
        result += f"💰 总未实现盈亏: {total_pnl:+.2f} USDC\n\n"
        
        result += "【持仓详情】\n"
        for pos in positions_data.get("positions", []):
            symbol = pos.get('market', 'Unknown')
            side = pos.get('side', 'Unknown')
            size = pos.get('size', '0')
            entry_price = pos.get('entry_price', '0')
            mark_price = pos.get('mark_price', '0')
            pnl = pos.get('unrealized_pnl', '0')
            
            result += f"• {symbol}: {side} {size} @ {entry_price} (标记价: {mark_price}, 盈亏: {pnl})\n"
    
    result += f"\n🕒 数据时间: {positions_data.get('timestamp', 'N/A')}\n"
    return result


def format_trading_history_for_trader(history_data: Dict[str, Any]) -> str:
    """为交易员智能体格式化交易历史数据"""
    if history_data.get("error"):
        return f"⚠️ Paradex 交易历史获取失败: {history_data['error']}"
    
    if not history_data.get("success"):
        return "⚠️ 无法获取 Paradex 交易历史"
    
    result = "=== 📈 Paradex 交易历史分析 ===\n"
    
    analysis = history_data.get("analysis", {})
    total_trades = analysis.get("total_trades", 0)
    
    if total_trades == 0:
        result += "📭 最近无交易记录\n"
    else:
        buy_trades = analysis.get("buy_trades", 0)
        sell_trades = analysis.get("sell_trades", 0)
        realized_pnl = analysis.get("total_realized_pnl", 0)
        total_fees = analysis.get("total_fees", 0)
        most_active = analysis.get("most_active_symbol", "N/A")
        
        result += f"📊 交易统计:\n"
        result += f"• 总交易数: {total_trades} 笔\n"
        result += f"• 买入/卖出: {buy_trades}/{sell_trades} 笔\n"
        result += f"• 已实现盈亏: {realized_pnl:+.2f} USDC\n"
        result += f"• 总手续费: {total_fees:.2f} USDC\n"
        result += f"• 最活跃品种: {most_active}\n\n"
        
        # 显示最近几笔交易
        recent_trades = history_data.get("recent_trades", [])
        if recent_trades:
            result += "【最近交易】\n"
            for i, trade in enumerate(recent_trades[:3], 1):
                timestamp = datetime.fromtimestamp(int(trade.get('created_at', 0)) / 1000)
                symbol = trade.get('market', 'Unknown')
                side = trade.get('side', 'Unknown')
                size = trade.get('size', '0')
                price = trade.get('price', '0')
                
                result += f"{i}. {timestamp.strftime('%m-%d %H:%M')} {symbol} {side} {size} @ {price}\n"
    
    result += f"\n🕒 数据时间: {history_data.get('timestamp', 'N/A')}\n"
    return result


def format_open_orders_for_trader(orders_data: Dict[str, Any]) -> str:
    """为交易员智能体格式化挂单数据"""
    if orders_data.get("error"):
        return f"⚠️ Paradex 挂单数据获取失败: {orders_data['error']}"
    
    if not orders_data.get("success"):
        return "⚠️ 无法获取 Paradex 挂单数据"
    
    result = "=== 📋 Paradex 当前挂单状况 ===\n"
    
    total_orders = orders_data.get("total_orders", 0)
    
    if total_orders == 0:
        result += "📭 当前无挂单\n"
    else:
        analysis = orders_data.get("analysis", {})
        buy_orders = analysis.get("total_buy_orders", 0)
        sell_orders = analysis.get("total_sell_orders", 0)
        total_notional = analysis.get("total_notional_value", 0)
        
        result += f"📊 挂单统计:\n"
        result += f"• 总挂单数: {total_orders} 笔\n"
        result += f"• 买单/卖单: {buy_orders}/{sell_orders} 笔\n"
        result += f"• 总名义价值: {total_notional:,.2f} USDC\n\n"
        
        # 显示挂单详情
        orders = orders_data.get("orders", [])
        if orders:
            result += "【挂单详情】\n"
            for i, order in enumerate(orders[:10], 1):  # 最多显示10个挂单
                order_id = order.get('id', 'Unknown')[:8]  # 显示订单ID前8位
                market = order.get('market', 'Unknown')
                side = order.get('side', 'Unknown')
                order_type = order.get('type', 'LIMIT')
                size = order.get('size', '0')
                price = order.get('price', '0')
                filled = order.get('filled_size', '0')
                status = order.get('status', 'Unknown')
                
                result += f"{i}. [{order_id}] {market}: {side} {order_type} {size} @ {price}"
                if float(filled) > 0:
                    result += f" (已成交: {filled})"
                result += f" - {status}\n"
    
    result += f"\n🕒 数据时间: {orders_data.get('timestamp', 'N/A')}\n"
    return result


def format_portfolio_insights_for_trader(overview_data: Dict[str, Any]) -> str:
    """为交易员智能体格式化投资组合洞察"""
    if overview_data.get("error"):
        return f"⚠️ 投资组合数据获取失败: {overview_data['error']}"
    
    result = "=== 💡 Paradex 投资组合洞察 ===\n"
    
    insights = overview_data.get("insights", [])
    if insights:
        for insight in insights:
            result += f"{insight}\n"
    else:
        result += "暂无洞察数据\n"
    
    result += f"\n🕒 分析时间: {overview_data.get('timestamp', 'N/A')}\n"
    return result