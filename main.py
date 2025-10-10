from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG

# 导入日志模块
from tradingagents.utils.logging_manager import get_logger
logger = get_logger('default')


# Create a custom config
config = DEFAULT_CONFIG.copy()
config["llm_provider"] = "deepseek"  # Use a different model
config["deepseek_api_key"] = "sk-xxxxxx"  # Use a different backend
config["deep_think_llm"] = "deepseek-chat"  # Use a different model
config["quick_think_llm"] = "deepseek-chat"  # Use a different model
config["max_debate_rounds"] = 1  # Increase debate rounds
config["online_tools"] = True  # Increase debate rounds

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
final_state, decision = ta.propagate("000001", "2025-10-09")
ta._log_state("2025-10-09", final_state)
print(ta.log_states_dict["2025-10-09"])
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
