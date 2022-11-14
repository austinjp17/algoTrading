import requests

API_KEY = "C1D89F0B-818A-4DC8-818B-6D356B576DC2"
baseUrl = "http://rest.coinapi.io/"

def order_book(symbol_id,limit,limit_levels):
    
    endpoint = f"v1/orderbooks/{symbol_id}/latest?limit={limit}&limit_levels={limit_levels}"
    headers = {
        'X-CoinAPI-Key' : API_KEY,
        'Accept':"application/json",
    }
    reqUrl = baseUrl + endpoint
    # reqUrl = "https://rest.coinapi.io/v1/assets"
    orderBook = requests.get(reqUrl, headers=headers).json()
    return orderBook



if __name__ == "__main__":
    
    symbol_id = "BITSTAMP_SPOT_BTC_USD"
    limit = 10
    limit_levels=5
    resp = order_book(symbol_id=symbol_id,limit=limit,limit_levels=limit_levels)
    for tick in resp:
        print(f"\n\nExchange Time: {tick['time_exchange']}\nAPI Time: {tick['time_coinapi']}")
        print("---- Asks ----")
        for bid in tick["asks"]:
            price = bid["price"]
            sz = bid["size"]
            print(f"price: {price}\nsize: {sz}")
        print("---- Bids ----")
        for bid in tick["bids"]:
            price = bid["price"]
            sz = bid["size"]
            print(f"price: {price}\nsize: {sz}")
        

