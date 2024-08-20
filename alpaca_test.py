from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, StockTradesRequest
from datetime import datetime
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, OrderType, TimeInForce

# Change this up for the session
api_key = "PKTYN32DJDJB8Z8JLGXL"
api_secret_key = "NbbtORcQJk1LeQzOPSYBZOp9XtuDLCa0I04wuxV6"

# API key and secret key
trading_client = TradingClient(api_key, api_secret_key)
market_order = MarketOrderRequest(
    symbol = "ASTS",
    qty = 1,
    side = OrderSide.BUY,
    time_in_force = TimeInForce.DAY
)

order_exec = trading_client.submit_order(market_order)
print(order_exec)
#print("Account number : " + trading_client.get_account().account_number)
#print("Buying Power : " + trading_client.get_account().buying_power)


# Sample Stock Data Call
""" 
data_client = StockHistoricalDataClient("PK8OO53K48MOP3AKSD12", "MuBKPl41JKbOaBX6EKcCLMa1NcP47J5UfppEHMFm")
request_params = StockTradesRequest(
    symbol_or_symbols="ASTS",
    start=datetime(2024, 8, 20, 13, 0),
    end = datetime(2024, 8, 20, 13, 15),
    limit=10
)

trades = data_client.get_stock_trades(request_params)

for trade in trades.data["ASTS"]:
    print(trade) """



