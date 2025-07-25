#!/usr/bin/env python
"""
测试改进后的 OpenRouter 集成
验证新闻获取函数是否能正确处理 OpenRouter 的 Web Search
"""

import os
import sys
from datetime import datetime, timedelta
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 添加项目路径
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tradingagents.dataflows.config import get_config, initialize_config
from tradingagents.dataflows import interface


def test_openrouter_integration():
    """测试 OpenRouter 集成是否正常工作"""
    
    # 初始化配置
    initialize_config()
    config = get_config()
    
    # 测试参数
    test_ticker = "AAPL"
    test_date = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
    
    print("="*60)
    print("OpenRouter 集成测试")
    print(f"Backend URL: {config.get('backend_url')}")
    print(f"Model: {config.get('quick_think_llm')}")
    print(f"测试股票: {test_ticker}")
    print(f"测试日期: {test_date}")
    print("="*60)
    
    # 测试函数列表
    test_functions = [
        ("股票新闻", lambda: interface.get_stock_news_openai(test_ticker, test_date)),
        ("全球新闻", lambda: interface.get_global_news_openai(test_date)),
        ("基本面数据", lambda: interface.get_fundamentals_openai(test_ticker, test_date))
    ]
    
    results = []
    
    for func_name, func in test_functions:
        print(f"\n测试 {func_name}...")
        try:
            result = func()
            success = True
            error_msg = None
            
            # 检查结果是否有效
            if result and isinstance(result, str) and len(result) > 10:
                print(f"✓ 成功 - 返回了 {len(result)} 个字符的内容")
                print(f"  预览: {result[:100]}...")
            else:
                success = False
                error_msg = f"返回内容无效: {result}"
                print(f"✗ 失败 - {error_msg}")
                
        except Exception as e:
            success = False
            error_msg = str(e)
            print(f"✗ 失败 - 错误: {error_msg}")
        
        results.append({
            "function": func_name,
            "success": success,
            "error": error_msg
        })
    
    # 打印总结
    print("\n" + "="*60)
    print("测试总结")
    print("="*60)
    
    success_count = sum(1 for r in results if r["success"])
    total_count = len(results)
    
    print(f"成功率: {success_count}/{total_count}")
    
    for result in results:
        status = "✓" if result["success"] else "✗"
        print(f"{status} {result['function']}")
        if not result["success"] and result["error"]:
            print(f"   错误: {result['error']}")
    
    print("\n提示：")
    if "openrouter" in config.get("backend_url", "").lower():
        print("- 当前使用 OpenRouter，将使用 :online 后缀或 plugins 参数")
    else:
        print("- 当前使用标准 backend，将使用 responses.create API")
    
    return success_count == total_count


def main():
    """主函数"""
    # 检查 API 密钥
    if not os.getenv("OPENAI_API_KEY"):
        print("错误: 未找到 OPENAI_API_KEY 环境变量")
        print("请在 .env 文件中设置 OPENAI_API_KEY")
        return
    
    # 运行测试
    success = test_openrouter_integration()
    
    if success:
        print("\n✅ 所有测试通过！OpenRouter 集成正常工作。")
    else:
        print("\n❌ 部分测试失败，请检查错误信息。")


if __name__ == "__main__":
    main()