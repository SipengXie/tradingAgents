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

    def preview_chromadb_deletion(self, decision_id: str, config: dict) -> dict:
        """
        预览删除某个decision_id对应的ChromaDB记录

        Args:
            decision_id: 决策ID
            config: 项目配置

        Returns:
            预览结果字典，包含每个collection将删除的记录信息
        """
        try:
            from tradingagents.agents.utils.memory import FinancialSituationMemory
            import chromadb
            from chromadb.config import Settings

            # 获取ChromaDB客户端
            persist_directory = config.get("memory_persist_dir",
                                          Path(config.get("project_dir", ".")) / "memory_db")
            chroma_client = chromadb.PersistentClient(
                path=str(persist_directory),
                settings=Settings(allow_reset=True)
            )

            memory_components = [
                "bull_memory",
                "bear_memory",
                "trader_memory",
                "invest_judge_memory",
                "risk_manager_memory"
            ]

            preview_results = {}

            for memory_name in memory_components:
                try:
                    collection = chroma_client.get_collection(name=memory_name)

                    # 通过decision_id查询记录
                    results = collection.get(
                        where={"decision_id": decision_id},
                        include=["metadatas", "documents"]
                    )

                    if results and results['ids']:
                        preview_results[memory_name] = {
                            "count": len(results['ids']),
                            "ids": results['ids'],
                            "sample_text": results['documents'][0][:200] + "..." if results['documents'] else ""
                        }
                    else:
                        preview_results[memory_name] = {
                            "count": 0,
                            "ids": [],
                            "sample_text": ""
                        }

                except Exception as e:
                    preview_results[memory_name] = {
                        "count": 0,
                        "ids": [],
                        "error": str(e)
                    }

            return {
                "success": True,
                "decision_id": decision_id,
                "preview": preview_results,
                "total_records": sum(r.get("count", 0) for r in preview_results.values())
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"预览失败: {str(e)}"
            }

    def delete_chromadb_records(self, decision_id: str, config: dict) -> dict:
        """
        删除某个decision_id对应的所有ChromaDB记录

        Args:
            decision_id: 决策ID
            config: 项目配置

        Returns:
            删除结果字典
        """
        try:
            import chromadb
            from chromadb.config import Settings

            # 获取ChromaDB客户端
            persist_directory = config.get("memory_persist_dir",
                                          Path(config.get("project_dir", ".")) / "memory_db")
            chroma_client = chromadb.PersistentClient(
                path=str(persist_directory),
                settings=Settings(allow_reset=True)
            )

            memory_components = [
                "bull_memory",
                "bear_memory",
                "trader_memory",
                "invest_judge_memory",
                "risk_manager_memory"
            ]

            deletion_results = {}
            total_deleted = 0

            for memory_name in memory_components:
                try:
                    collection = chroma_client.get_collection(name=memory_name)

                    # 通过decision_id查询记录
                    results = collection.get(
                        where={"decision_id": decision_id}
                    )

                    if results and results['ids']:
                        # 删除找到的记录
                        collection.delete(ids=results['ids'])
                        deleted_count = len(results['ids'])
                        total_deleted += deleted_count

                        deletion_results[memory_name] = {
                            "deleted": deleted_count,
                            "ids": results['ids']
                        }
                    else:
                        deletion_results[memory_name] = {
                            "deleted": 0,
                            "ids": []
                        }

                except Exception as e:
                    deletion_results[memory_name] = {
                        "deleted": 0,
                        "error": str(e)
                    }

            return {
                "success": True,
                "decision_id": decision_id,
                "deletion_results": deletion_results,
                "total_deleted": total_deleted
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"删除ChromaDB记录失败: {str(e)}"
            }

    def delete_learning_record_complete(self, record_file_path: str, config: dict) -> dict:
        """
        完整删除学习记录（JSON文件 + ChromaDB记录）

        Args:
            record_file_path: 学习记录JSON文件的完整路径
            config: 项目配置

        Returns:
            删除结果字典
        """
        try:
            record_path = Path(record_file_path)

            if not record_path.exists():
                return {
                    "success": False,
                    "error": "学习记录文件不存在"
                }

            # 读取学习记录获取decision_id
            with open(record_path, 'r', encoding='utf-8') as f:
                record = json.load(f)

            decision_id = record.get('decision_id')

            if not decision_id:
                # 旧记录，没有decision_id，只能删除JSON文件
                record_path.unlink()
                return {
                    "success": True,
                    "is_legacy": True,
                    "json_deleted": str(record_path.name),
                    "chromadb_deleted": 0,
                    "message": "⚠️ 旧记录（无decision_id），仅删除了JSON文件"
                }

            # 新记录，先删除ChromaDB数据
            chromadb_result = self.delete_chromadb_records(decision_id, config)

            if not chromadb_result.get('success'):
                return {
                    "success": False,
                    "error": f"删除ChromaDB记录失败: {chromadb_result.get('error')}"
                }

            # 然后删除JSON文件
            record_path.unlink()

            return {
                "success": True,
                "is_legacy": False,
                "decision_id": decision_id,
                "json_deleted": str(record_path.name),
                "chromadb_deleted": chromadb_result.get('total_deleted', 0),
                "deletion_details": chromadb_result.get('deletion_results', {}),
                "message": f"✅ 成功删除学习记录（ChromaDB: {chromadb_result.get('total_deleted', 0)}条, JSON: 1个文件）"
            }

        except Exception as e:
            return {
                "success": False,
                "error": f"删除学习记录失败: {str(e)}"
            }
