import requests
import pandas as pd
from datetime import datetime

class CryptoFetcher:
    @staticmethod
    def fetch_crypto_history(crypto_id):
        url = f"https://api.coingecko.com/api/v3/coins/{crypto_id}/market_chart"
        params = {
            "vs_currency": "usd",
            "days": "30",
            "interval": "daily"
        }
        response = requests.get(url, params=params)
        data = response.json()

        prices = data.get("prices", [])

        result = []
        for timestamp, price in prices:
            date = datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')
            result.append({"date": date, "price": price})

        return pd.DataFrame(result)
