import os
import json
import time
import requests
from dotenv import load_dotenv
import oandapyV20
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.pricing as pricing

# 環境変数の読み込み
load_dotenv()

# OANDA API設定
OANDA_API_KEY = os.getenv("OANDA_API_KEY")
ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID")
OANDA_URL = "https://api-fxtrade.oanda.com/v3"

# APIクライアントの作成
client = oandapyV20.API(access_token=OANDA_API_KEY)

# 注文関数
def place_order(instrument="EUR_USD", units=100, order_type="MARKET", side="buy"):
    """OANDAに注文を送信"""
    data = {
        "order": {
            "instrument": instrument,
            "units": units if side == "buy" else -units,
            "type": order_type,
            "positionFill": "DEFAULT"
        }
    }
    r = orders.OrderCreate(accountID=ACCOUNT_ID, data=data)
    client.request(r)
    return r.response


# 自動売買の開始
if __name__ == "__main__":
    auto_trade()
