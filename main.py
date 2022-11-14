from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce

API_KEY = "PK2M90YALR6Z1GTXCNO9"
SECRET_KEY = "TQdnubOiHO1fgCXvgK5996RgTHIwmu7ppXMLsLFG"
ENDPOINT = "https://paper-api.alpaca.markets"

trading_client = TradingClient(API_KEY, SECRET_KEY, paper=True)
account = trading_client.get_account()
market_order_data = MarketOrderRequest(
                      symbol="BTC/USD",
                      qty=1,
                      side=OrderSide.BUY,
                      time_in_force=TimeInForce.GTC
                  )
market_order = trading_client.submit_order(market_order_data)
for property_name, value in account:
  print(f"\"{property_name}\": {value}")