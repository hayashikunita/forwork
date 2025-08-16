from fastmcp import FastMCP
from pydantic import BaseModel, Field
from typing import Optional
import os
import json
import time
import requests
from dotenv import load_dotenv
import oandapyV20
import oandapyV20.endpoints.orders as orders
import oandapyV20.endpoints.pricing as pricing
from utils.websearch import web_search

# 環境変数の読み込み
load_dotenv()

# OANDA API設定
OANDA_API_KEY = os.getenv("OANDA_API_KEY")
ACCOUNT_ID = os.getenv("OANDA_ACCOUNT_ID")
OANDA_URL = "https://api-fxtrade.oanda.com/v3"

# APIクライアントの作成
client = oandapyV20.API(access_token=OANDA_API_KEY)
mcp = FastMCP("call-oanda-server")


currency_list = ["EUR_USD","USD_JPY","GBP_USD","USD_CHF","USD_CAD","AUD_USD","NZD_USD","EUR_JPY","GBP_JPY","AUD_JPY","EUR_GBP","EUR_AUD","CHF_JPY","USD_TRY","USD_MXN","USD_ZAR","USD_SGD","EUR_NOK"]
description_prompt_get_price = """
指定した通貨ペアから価格を取得するツールです。
引数：str
sample_input : "EUR_USD"
"""
add_info =f'入力される値はこのリスト{currency_list}のうちの１つとする。'
description_prompt_get_price += add_info 
@mcp.tool(
    name="get-price-from-oanda",
    description = description_prompt_get_price, 
    tags={"price"}    
)
def get_price(
    instrument: str = Field(description=f'指定した通貨ペアが入力される。入力される値はこのリストのうちの１つとする。：{currency_list}')
    ) -> str:
    params = {"instruments": instrument}
    r = pricing.PricingInfo(accountID=ACCOUNT_ID, params=params)
    client.request(r)
    prices = r.response["prices"]
    bid_price = float(prices[0]["bids"][0]["price"])
    ask_price = float(prices[0]["asks"][0]["price"])
    return bid_price, ask_price



description_prompt_order = """
指定した通貨ペアから発注するツールです。
sampleの引数：
    instrument:"EUR_USD",
    units: 100 ,
    order_type ="MARKET",
    side: "buy"
"""
buy_or_sell =["buy","sell"]
add_info =f'instrumentには、{currency_list}のうちの1つとする。unitsには、Integerが入る。order_typeは常に"market"が入る。sideには、{buy_or_sell}から一つ入る。'
description_prompt_order += add_info 
@mcp.tool(
        name="order-from-oanda",
        description = description_prompt_order, 
        tags={"order"}
        )
def place_order(
    instrument: str = Field(description=f'指定した通貨ペアが入力される。入力される値はこのリストのうちの１つとする。：{currency_list}'),
    units: int = Field(description="Maximum number of results", ge=1, le=100),
    side: str = Field(description=f'buyまたはsellが入る。：{buy_or_sell}')
    ) -> str:
    data = {
        "order": {
            "instrument": instrument,
            "units": units if side == "buy" else -units,
    side: str = Field(description=f'buyまたはsellが入る。：{buy_or_sell}'),
    order_type: str = Field(default="market", description='Order type, e.g., "market", "limit", etc.')
    ) -> str:
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

if __name__ == "__main__":
    mcp.run()