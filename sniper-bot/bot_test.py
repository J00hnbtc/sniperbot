# bot_test.py
import asyncio
from config import CONFIG

async def simulate_trade(symbol, amount):
    print(f"[SIMULATION] 📈 Achat simulé de {symbol} pour {amount}$")

async def main():
    print("🔧 Démarrage du bot en mode SIMULATION...")
    for pair in CONFIG["TRADING_PAIRS"]:
        await simulate_trade(pair, CONFIG["DEFAULT_ALLOCATION_USD"])
    print("✅ Fin de la simulation.")

if __name__ == "__main__":
    asyncio.run(main())
