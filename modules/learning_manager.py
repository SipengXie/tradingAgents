"""
学习记录管理器
管理手动学习记录的加载、过滤、删除等操作
"""

import json
from pathlib import Path


class LearningRecordManager:
    """学习记录管理器"""

    def __init__(self, eval_results_dir: str = "eval_results"):
        """
        初始化学习记录管理器

        Args:
            eval_results_dir: eval_results 目录路径
        """
        self.eval_results_dir = Path(eval_results_dir)

    def load_learning_records(self) -> list[dict]:
        """
        加载所有手动学习记录

        Returns:
            学习记录列表，按时间戳排序（最新的在前）
        """
        learning_records = []

        if not self.eval_results_dir.exists():
            return learning_records

        # 查找所有手动学习记录文件
        for record_file in self.eval_results_dir.glob("manual_learning_*.json"):
            try:
                with open(record_file, 'r', encoding='utf-8') as f:
                    record = json.load(f)
                    record['file_name'] = record_file.name
                    record['file_path'] = str(record_file)
                    learning_records.append(record)
            except Exception:
                # 静默跳过无法读取的文件
                pass

        # 按时间戳排序（最新的在前）
        learning_records.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        return learning_records

    def get_learned_decision_logs(self) -> set[str]:
        """
        获取已经学习过的决策日志路径集合

        Returns:
            已学习的决策日志文件路径集合
        """
        learned_logs = set()
        learning_records = self.load_learning_records()

        for record in learning_records:
            if record.get('success') and record.get('decision_log_path'):
                learned_logs.add(record['decision_log_path'])

        return learned_logs

    def filter_unlearned_logs(self, all_logs: list[dict]) -> list[dict]:
        """
        过滤出未学习过的决策日志

        Args:
            all_logs: 所有决策日志列表

        Returns:
            未学习过的决策日志列表
        """
        learned_logs = self.get_learned_decision_logs()
        unlearned_logs = []

        for log in all_logs:
            if log.get('file_path') not in learned_logs:
                unlearned_logs.append(log)

        return unlearned_logs

    def mark_learned_logs(self, all_logs: list[dict]) -> list[dict]:
        """
        标记已学习的决策日志

        Args:
            all_logs: 所有决策日志列表

        Returns:
            添加了 is_learned 标记的决策日志列表
        """
        learned_logs = self.get_learned_decision_logs()

        for log in all_logs:
            log['is_learned'] = log.get('file_path') in learned_logs

        return all_logs

    def delete_decision_log(self, log_file_path: str) -> tuple[bool, str]:
        """
        删除决策日志文件

        Args:
            log_file_path: 决策日志文件的完整路径

        Returns:
            (成功标志, 消息)
        """
        try:
            log_path = Path(log_file_path)

            if not log_path.exists():
                return False, "日志文件不存在"

            # 删除文件
            log_path.unlink()

            return True, f"成功删除日志文件: {log_path.name}"

        except Exception as e:
            return False, f"删除日志文件失败: {str(e)}"

    def delete_related_learning_records(self, log_file_path: str) -> tuple[int, list]:
        """
        删除与指定决策日志相关的学习记录

        Args:
            log_file_path: 决策日志文件的完整路径

        Returns:
            (删除数量, 错误列表)
        """
        deleted_count = 0
        errors = []

        try:
            if not self.eval_results_dir.exists():
                return 0, []

            # 遍历所有学习记录文件
            for record_file in self.eval_results_dir.glob("manual_learning_*.json"):
                try:
                    with open(record_file, 'r', encoding='utf-8') as f:
                        record = json.load(f)

                    # 检查是否关联到要删除的决策日志
                    if record.get('decision_log_path') == log_file_path:
                        record_file.unlink()
                        deleted_count += 1

                except Exception as e:
                    errors.append(f"处理 {record_file.name} 时出错: {str(e)}")

            return deleted_count, errors

        except Exception as e:
            errors.append(f"扫描学习记录时出错: {str(e)}")
            return deleted_count, errors
