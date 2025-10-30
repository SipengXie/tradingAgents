"""
工具执行监控和日志系统
提供工具调用日志记录、性能统计和健康检查功能
"""
import logging
import time
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional, Callable
from functools import wraps
from collections import defaultdict
import threading

logger = logging.getLogger(__name__)


class ToolMonitor:
    """工具执行监控器"""

    def __init__(self, log_dir: str = "logs/tool_execution"):
        """
        初始化工具监控器

        Args:
            log_dir: 日志文件存储目录
        """
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        # 统计数据（线程安全）
        self._lock = threading.Lock()
        self.execution_stats = defaultdict(lambda: {
            'total_calls': 0,
            'successful_calls': 0,
            'failed_calls': 0,
            'total_time': 0.0,
            'avg_time': 0.0,
            'last_success': None,
            'last_failure': None,
            'error_messages': []
        })

        # 保存文件处理器引用以便清理
        self._file_handler = None

        # 配置日志文件
        self._setup_logging()

    def _setup_logging(self):
        """配置日志处理器（带资源清理）"""
        log_file = self.log_dir / f"tool_execution_{datetime.now().strftime('%Y%m%d')}.log"

        # 获取tool_logger
        tool_logger = logging.getLogger('tool_execution')

        # 清除该logger的所有旧handlers（防止重复添加）
        if tool_logger.handlers:
            for handler in tool_logger.handlers[:]:
                handler.close()
                tool_logger.removeHandler(handler)

        tool_logger.setLevel(logging.INFO)

        # 创建新的文件处理器
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.INFO)

        # 创建格式化器
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        file_handler.setFormatter(formatter)

        # 添加处理器到logger
        tool_logger.addHandler(file_handler)

        self.tool_logger = tool_logger
        self._file_handler = file_handler

    def __del__(self):
        """析构函数：清理资源"""
        try:
            if hasattr(self, '_file_handler') and self._file_handler:
                self._file_handler.close()

            if hasattr(self, 'tool_logger') and self.tool_logger:
                # 移除所有handlers
                for handler in self.tool_logger.handlers[:]:
                    handler.close()
                    self.tool_logger.removeHandler(handler)
        except Exception as e:
            # 在析构函数中不应抛出异常
            logger.error(f"清理ToolMonitor资源时出错: {e}")

    def log_tool_call(
        self,
        tool_name: str,
        params: Dict[str, Any],
        result: Optional[str] = None,
        error: Optional[Exception] = None,
        execution_time: Optional[float] = None
    ):
        """
        记录工具调用

        Args:
            tool_name: 工具名称
            params: 调用参数
            result: 执行结果（可选）
            error: 错误信息（可选）
            execution_time: 执行时间（秒）
        """
        timestamp = datetime.now().isoformat()
        success = error is None

        # 构建日志条目
        log_entry = {
            'timestamp': timestamp,
            'tool_name': tool_name,
            'params': params,
            'success': success,
            'execution_time': execution_time,
        }

        if result:
            # 截断过长的结果
            log_entry['result_preview'] = result[:200] + '...' if len(result) > 200 else result
            log_entry['result_length'] = len(result)

        if error:
            log_entry['error'] = str(error)
            log_entry['error_type'] = type(error).__name__

        # 记录到文件
        self.tool_logger.info(json.dumps(log_entry, ensure_ascii=False))

        # 更新统计数据
        self._update_stats(tool_name, success, execution_time, error)

    def _update_stats(
        self,
        tool_name: str,
        success: bool,
        execution_time: Optional[float],
        error: Optional[Exception]
    ):
        """更新工具统计数据"""
        with self._lock:
            stats = self.execution_stats[tool_name]
            stats['total_calls'] += 1

            if success:
                stats['successful_calls'] += 1
                stats['last_success'] = datetime.now().isoformat()
            else:
                stats['failed_calls'] += 1
                stats['last_failure'] = datetime.now().isoformat()
                if error:
                    error_msg = f"{type(error).__name__}: {str(error)}"
                    stats['error_messages'].append({
                        'timestamp': datetime.now().isoformat(),
                        'message': error_msg
                    })
                    # 只保留最近10条错误
                    stats['error_messages'] = stats['error_messages'][-10:]

            if execution_time:
                stats['total_time'] += execution_time
                stats['avg_time'] = stats['total_time'] / stats['total_calls']

    def get_stats(self, tool_name: Optional[str] = None) -> Dict[str, Any]:
        """
        获取工具统计数据

        Args:
            tool_name: 工具名称，如果为None则返回所有工具的统计

        Returns:
            统计数据字典
        """
        with self._lock:
            if tool_name:
                return dict(self.execution_stats.get(tool_name, {}))
            else:
                return {
                    name: dict(stats)
                    for name, stats in self.execution_stats.items()
                }

    def get_health_status(self) -> Dict[str, str]:
        """
        获取所有工具的健康状态

        Returns:
            工具健康状态字典，格式：{tool_name: 'healthy'/'warning'/'critical'}
        """
        health_status = {}

        with self._lock:
            for tool_name, stats in self.execution_stats.items():
                total = stats['total_calls']
                if total == 0:
                    health_status[tool_name] = 'unknown'
                    continue

                success_rate = stats['successful_calls'] / total

                if success_rate >= 0.9:
                    health_status[tool_name] = 'healthy'
                elif success_rate >= 0.7:
                    health_status[tool_name] = 'warning'
                else:
                    health_status[tool_name] = 'critical'

        return health_status

    def reset_stats(self, tool_name: Optional[str] = None):
        """
        重置统计数据

        Args:
            tool_name: 工具名称，如果为None则重置所有统计
        """
        with self._lock:
            if tool_name:
                if tool_name in self.execution_stats:
                    del self.execution_stats[tool_name]
            else:
                self.execution_stats.clear()

    def export_stats(self, output_file: Optional[str] = None) -> str:
        """
        导出统计数据到JSON文件

        Args:
            output_file: 输出文件路径，如果为None则使用默认路径

        Returns:
            输出文件路径
        """
        if output_file is None:
            output_file = self.log_dir / f"tool_stats_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        else:
            output_file = Path(output_file)

        stats = self.get_stats()
        health = self.get_health_status()

        export_data = {
            'export_time': datetime.now().isoformat(),
            'statistics': stats,
            'health_status': health
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)

        logger.info(f"统计数据已导出到: {output_file}")
        return str(output_file)


# 全局工具监控器实例
_global_monitor = None


def get_tool_monitor(log_dir: str = "logs/tool_execution") -> ToolMonitor:
    """
    获取全局工具监控器实例

    Args:
        log_dir: 日志目录

    Returns:
        ToolMonitor实例
    """
    global _global_monitor
    if _global_monitor is None:
        _global_monitor = ToolMonitor(log_dir)
    return _global_monitor


def monitor_tool(tool_func: Callable) -> Callable:
    """
    装饰器：监控工具执行

    使用方法：
    @monitor_tool
    @tool
    def my_tool(param1, param2):
        ...
    """
    @wraps(tool_func)
    def wrapper(*args, **kwargs):
        monitor = get_tool_monitor()
        tool_name = getattr(tool_func, 'name', tool_func.__name__)

        # 记录参数
        params = {
            'args': [str(arg)[:100] for arg in args],  # 截断长参数
            'kwargs': {k: str(v)[:100] for k, v in kwargs.items()}
        }

        start_time = time.time()
        result = None
        error = None

        try:
            # 执行工具
            result = tool_func(*args, **kwargs)
            return result
        except Exception as e:
            error = e
            raise
        finally:
            # 计算执行时间
            execution_time = time.time() - start_time

            # 记录日志
            monitor.log_tool_call(
                tool_name=tool_name,
                params=params,
                result=result,
                error=error,
                execution_time=execution_time
            )

    return wrapper


def check_tool_health() -> Dict[str, Any]:
    """
    检查所有工具的健康状态

    Returns:
        包含健康状态和统计的字典
    """
    monitor = get_tool_monitor()

    health_status = monitor.get_health_status()
    stats = monitor.get_stats()

    # 生成健康报告
    report = {
        'timestamp': datetime.now().isoformat(),
        'overall_health': 'healthy',  # 默认
        'tools': {}
    }

    critical_count = 0
    warning_count = 0

    for tool_name, status in health_status.items():
        tool_stats = stats.get(tool_name, {})

        report['tools'][tool_name] = {
            'health': status,
            'total_calls': tool_stats.get('total_calls', 0),
            'success_rate': (
                tool_stats.get('successful_calls', 0) / tool_stats.get('total_calls', 1)
                if tool_stats.get('total_calls', 0) > 0 else 0
            ),
            'avg_time': tool_stats.get('avg_time', 0),
            'last_success': tool_stats.get('last_success'),
            'last_failure': tool_stats.get('last_failure'),
        }

        if status == 'critical':
            critical_count += 1
        elif status == 'warning':
            warning_count += 1

    # 确定整体健康状态
    if critical_count > 0:
        report['overall_health'] = 'critical'
    elif warning_count > 0:
        report['overall_health'] = 'warning'

    report['summary'] = {
        'total_tools': len(health_status),
        'healthy': sum(1 for s in health_status.values() if s == 'healthy'),
        'warning': warning_count,
        'critical': critical_count,
        'unknown': sum(1 for s in health_status.values() if s == 'unknown'),
    }

    return report


# 命令行接口
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='工具监控系统')
    parser.add_argument('--stats', action='store_true', help='显示统计数据')
    parser.add_argument('--health', action='store_true', help='检查健康状态')
    parser.add_argument('--export', type=str, help='导出统计数据到文件')
    parser.add_argument('--reset', action='store_true', help='重置统计数据')

    args = parser.parse_args()

    monitor = get_tool_monitor()

    if args.stats:
        stats = monitor.get_stats()
        print(json.dumps(stats, indent=2, ensure_ascii=False))

    if args.health:
        health = check_tool_health()
        print(json.dumps(health, indent=2, ensure_ascii=False))

    if args.export:
        output_file = monitor.export_stats(args.export)
        print(f"统计数据已导出到: {output_file}")

    if args.reset:
        monitor.reset_stats()
        print("统计数据已重置")
