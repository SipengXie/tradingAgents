"""
Binance基础API封装
提供低级别的Binance API访问功能
"""

import os
from typing import Optional, Dict, List, Union, Any
from datetime import datetime, timedelta
import time
import logging
from functools import wraps

from binance.client import Client
from binance.exceptions import BinanceAPIException

logger = logging.getLogger(__name__)


class RateLimitException(Exception):
    """API频率限制异常"""
    pass


class MaxRetriesExceeded(Exception):
    """超过最大重试次数"""
    pass


def retry_on_rate_limit(max_retries: int = 3, initial_wait: float = 1.0):
    """
    装饰器：在遇到频率限制时自动重试
    
    Args:
        max_retries: 最大重试次数
        initial_wait: 初始等待时间（秒）
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            wait_time = initial_wait
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except BinanceAPIException as e:
                    last_exception = e
                    if e.code == -1003:  # TOO_MANY_REQUESTS
                        if attempt < max_retries:
                            logger.warning(f"触发频率限制，等待 {wait_time} 秒后重试...")
                            time.sleep(wait_time)
                            wait_time *= 2  # 指数退避
                        else:
                            raise MaxRetriesExceeded(f"超过最大重试次数: {e}")
                    else:
                        raise
                except Exception as e:
                    last_exception = e
                    if attempt < max_retries:
                        logger.warning(f"请求失败: {e}，重试 {attempt + 1}/{max_retries}")
                        time.sleep(wait_time)
                    else:
                        raise
            
            if last_exception:
                raise last_exception
                
        return wrapper
    return decorator


class BinanceAPIWrapper:
    """
    Binance API封装器
    提供带有重试机制的API访问
    """
    
    def __init__(self, api_key: Optional[str] = None, api_secret: Optional[str] = None):
        """
        初始化API封装器
        
        Args:
            api_key: API密钥（可选，将从环境变量读取）
            api_secret: API密钥（可选，将从环境变量读取）
        """
        # 优先使用传入的密钥，否则从环境变量读取
        self.api_key = api_key or os.getenv('BINANCE_API_KEY', '')
        self.api_secret = api_secret or os.getenv('BINANCE_API_SECRET', '')
        
        # 创建客户端
        self.client = Client(self.api_key, self.api_secret)
        self.authenticated = bool(self.api_key and self.api_secret)
        
        if not self.authenticated:
            logger.info("Binance客户端运行在公开模式（无API密钥）")
    
    # === 现货市场数据 API ===
    
    @retry_on_rate_limit()
    def get_exchange_info(self) -> Dict[str, Any]:
        """获取交易所信息"""
        return self.client.get_exchange_info()
    
    @retry_on_rate_limit()
    def get_symbol_info(self, symbol: str) -> Optional[Dict[str, Any]]:
        """获取特定交易对信息"""
        info = self.get_exchange_info()
        for s in info['symbols']:
            if s['symbol'] == symbol.upper():
                return s
        return None
    
    @retry_on_rate_limit()
    def get_klines(self, **params) -> List[List]:
        """获取K线数据"""
        return self.client.get_klines(**params)
    
    @retry_on_rate_limit()
    def get_historical_klines(self, symbol: str, interval: str, 
                            start_str: str, end_str: Optional[str] = None, 
                            limit: int = 1000) -> List[List]:
        """获取历史K线数据"""
        return self.client.get_historical_klines(
            symbol=symbol,
            interval=interval,
            start_str=start_str,
            end_str=end_str,
            limit=limit
        )
    
    @retry_on_rate_limit()
    def get_ticker(self, **params) -> Dict[str, Any]:
        """获取24小时价格变动"""
        return self.client.get_ticker(**params)
    
    @retry_on_rate_limit()
    def get_symbol_ticker(self, **params) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """获取交易对最新价格"""
        return self.client.get_symbol_ticker(**params)
    
    @retry_on_rate_limit()
    def get_order_book(self, **params) -> Dict[str, Any]:
        """获取订单簿"""
        return self.client.get_order_book(**params)
    
    @retry_on_rate_limit()
    def get_recent_trades(self, **params) -> List[Dict[str, Any]]:
        """获取最近成交"""
        return self.client.get_recent_trades(**params)
    
    @retry_on_rate_limit()
    def get_aggregate_trades(self, **params) -> List[Dict[str, Any]]:
        """获取聚合交易"""
        return self.client.get_aggregate_trades(**params)
    
    # === 期货市场数据 API ===
    
    @retry_on_rate_limit()
    def futures_exchange_info(self) -> Dict[str, Any]:
        """获取期货交易所信息"""
        return self.client.futures_exchange_info()
    
    @retry_on_rate_limit()
    def futures_klines(self, **params) -> List[List]:
        """获取期货K线数据"""
        return self.client.futures_klines(**params)
    
    @retry_on_rate_limit()
    def futures_ticker(self, **params) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """获取期货24小时价格变动"""
        return self.client.futures_ticker(**params)
    
    @retry_on_rate_limit()
    def futures_symbol_ticker(self, **params) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """获取期货最新价格"""
        return self.client.futures_symbol_ticker(**params)
    
    @retry_on_rate_limit()
    def futures_orderbook_ticker(self, **params) -> Union[Dict[str, Any], List[Dict[str, Any]]]:
        """获取期货最优挂单"""
        return self.client.futures_orderbook_ticker(**params)
    
    @retry_on_rate_limit()
    def futures_liquidation_orders(self, **params) -> List[Dict[str, Any]]:
        """获取强平订单"""
        return self.client.futures_liquidation_orders(**params)
    
    @retry_on_rate_limit()
    def futures_funding_rate(self, **params) -> List[Dict[str, Any]]:
        """获取资金费率历史"""
        return self.client.futures_funding_rate(**params)
    
    @retry_on_rate_limit()
    def futures_open_interest(self, **params) -> Dict[str, Any]:
        """获取持仓量"""
        return self.client.futures_open_interest(**params)
    
    @retry_on_rate_limit()
    def futures_open_interest_hist(self, **params) -> List[Dict[str, Any]]:
        """获取持仓量历史"""
        return self.client.futures_open_interest_hist(**params)
    
    @retry_on_rate_limit()
    def futures_top_longshort_position_ratio(self, **params) -> List[Dict[str, Any]]:
        """获取大户持仓量多空比"""
        return self.client.futures_top_longshort_position_ratio(**params)
    
    @retry_on_rate_limit()
    def futures_top_longshort_account_ratio(self, **params) -> List[Dict[str, Any]]:
        """获取大户账户数多空比"""
        return self.client.futures_top_longshort_account_ratio(**params)
    
    @retry_on_rate_limit()
    def futures_global_longshort_ratio(self, **params) -> List[Dict[str, Any]]:
        """获取多空持仓人数比"""
        return self.client.futures_global_longshort_ratio(**params)
    
    # === 账户相关 API (需要认证) ===
    
    @retry_on_rate_limit()
    def get_account(self, **params) -> Dict[str, Any]:
        """获取账户信息"""
        if not self.authenticated:
            raise ValueError("此操作需要API认证")
        return self.client.get_account(**params)
    
    @retry_on_rate_limit()
    def get_asset_balance(self, asset: str, **params) -> Dict[str, Any]:
        """获取特定资产余额"""
        if not self.authenticated:
            raise ValueError("此操作需要API认证")
        return self.client.get_asset_balance(asset=asset, **params)
    
    # === 辅助方法 ===
    
    def ping(self) -> Dict:
        """测试连接"""
        return self.client.ping()
    
    def get_server_time(self) -> Dict[str, int]:
        """获取服务器时间"""
        return self.client.get_server_time()
    
    def get_system_status(self) -> Dict[str, Any]:
        """获取系统状态"""
        return self.client.get_system_status()


# 全局实例缓存
import threading
_api_wrapper_instance = None
_api_wrapper_lock = threading.Lock()

def get_binance_api() -> BinanceAPIWrapper:
    """
    获取Binance API封装器的单例实例（线程安全）

    Returns:
        BinanceAPIWrapper实例
    """
    global _api_wrapper_instance
    if _api_wrapper_instance is None:
        with _api_wrapper_lock:
            # Double-checked locking
            if _api_wrapper_instance is None:
                _api_wrapper_instance = BinanceAPIWrapper()
    return _api_wrapper_instance