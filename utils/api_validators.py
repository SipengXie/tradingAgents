"""
API 验证器
提供各种 API 连接测试功能
"""

from openai import OpenAI
import finnhub


class APIValidator:
    """API 连接验证器"""

    @staticmethod
    def test_llm_api(backend_url: str, api_key: str, model: str) -> tuple[bool, str]:
        """
        测试 LLM API 是否可用

        Args:
            backend_url: LLM API 后端 URL
            api_key: API 密钥
            model: 模型名称

        Returns:
            (成功标志, 消息)
        """
        try:
            client = OpenAI(
                base_url=backend_url,
                api_key=api_key
            )
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": "Hello"}],
                max_tokens=10
            )
            return True, "LLM API 连接成功"
        except Exception as e:
            return False, f"LLM API 连接失败: {str(e)}"

    @staticmethod
    def test_embedding_api(embedding_url: str, api_key: str, model: str) -> tuple[bool, str]:
        """
        测试 Embedding API 是否可用

        Args:
            embedding_url: Embedding API URL
            api_key: API 密钥
            model: 嵌入模型名称

        Returns:
            (成功标志, 消息)
        """
        try:
            client = OpenAI(
                base_url=embedding_url,
                api_key=api_key
            )
            response = client.embeddings.create(
                model=model,
                input="test"
            )
            return True, "Embedding API 连接成功"
        except Exception as e:
            return False, f"Embedding API 连接失败: {str(e)}"

    @staticmethod
    def test_finnhub_api(api_key: str) -> tuple[bool, str]:
        """
        测试 Finnhub API 是否可用

        Args:
            api_key: Finnhub API 密钥

        Returns:
            (成功标志, 消息)
        """
        try:
            finnhub_client = finnhub.Client(api_key=api_key)
            # 测试获取苹果股票报价
            quote = finnhub_client.quote('AAPL')
            if quote and 'c' in quote:
                return True, "Finnhub API 连接成功"
            else:
                return False, "Finnhub API 返回数据异常"
        except Exception as e:
            return False, f"Finnhub API 连接失败: {str(e)}"

    @staticmethod
    def test_binance_api(api_key: str, api_secret: str) -> tuple[bool, str]:
        """
        测试 Binance API 是否可用

        Args:
            api_key: Binance API 密钥
            api_secret: Binance API Secret

        Returns:
            (成功标志, 消息)
        """
        try:
            from tradingagents.dataflows.binance_utils import BinanceAPIWrapper

            # 创建 API 包装器
            api = BinanceAPIWrapper(api_key=api_key, api_secret=api_secret)

            # 测试基本连接
            ping_result = api.ping()
            if ping_result != {}:
                return False, "Binance API ping 响应异常"

            # 测试服务器时间
            server_time = api.get_server_time()
            if not server_time or 'serverTime' not in server_time:
                return False, "Binance API 服务器时间获取失败"

            # 如果提供了密钥，测试认证
            if api_key and api_secret:
                try:
                    # 测试获取账户信息
                    account = api.client.get_account()
                    if account and 'balances' in account:
                        return True, "Binance API 连接成功（已认证）"
                except Exception as auth_error:
                    # 认证失败但基本连接成功
                    if "APIError" in str(auth_error):
                        return True, f"Binance API 连接成功（认证失败: {str(auth_error)[:50]}...）"

            return True, "Binance API 连接成功（公共接口）"

        except ImportError:
            return False, "Binance 库未安装，请运行: pip install python-binance"
        except Exception as e:
            return False, f"Binance API 连接失败: {str(e)}"
