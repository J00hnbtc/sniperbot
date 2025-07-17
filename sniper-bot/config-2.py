# config.py
import os

CONFIG = {
    "PRIVATE_KEY": os.getenv("PRIVATE_KEY"),
    "BSC_RPC": os.getenv("BSC_RPC"),
    "SIMULATION_MODE": os.getenv("SIMULATION_MODE", "True") == "True",
    "TELEGRAM_TOKEN": os.getenv("TELEGRAM_TOKEN"),
    "TELEGRAM_CHAT_ID": os.getenv("TELEGRAM_CHAT_ID"),
    "DEFAULT_ALLOCATION_USD": 100,  # Pour le test
    "MIN_LIQUIDITY_USD": 50000,
    "MAX_SLIPPAGE": 0.10,
    "STOP_LOSS_PERCENT": 0.20,
    "TRADING_PAIRS": ["WBNB/USDT", "PEPE/BNB", "FLOKI/BNB"]
}
