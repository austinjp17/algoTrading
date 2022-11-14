import pandas as pd

from alpaca.data.historical import CryptoHistoricalDataClient

request_params = CryptoBarsRequest(
                        symbol_or_symbols=["BTC/USD"],
                        timeframe=TimeFrame.Day,
                        start="2022-09-01",
                        end="2022-09-07"
                        )
btc_bars = client.get_crypto_bars(request_params)

# Convert to dataframe
btc_bars.df


