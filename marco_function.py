import json
import pandas as pd
import requests

# File works locally for personal key and must call its own exchange 
# data within function replacing "NYSE" with the desired exchange. 
# I have not yet found a way to call the exchange data within 
# the function without hardcoding the exchange name, but I will continue to work on it. 
#test
def get_exchange_data(key):
    """
    returns metadata for a specific exchange
    available: US, NASDAQ, OTCBB, PINK, BATS
    """
    endpoint = f"https://eodhd.com/api/exchange-symbol-list/NYSE?api_token=69fcb2e0ef9372.85557703&fmt=json"
    print("Downloading data")
    call = requests.get(endpoint).text
    exchange_data = pd.DataFrame(json.loads(call))
    print("Completed")
    return exchange_data

def main():
    key = open('api_token.txt').read()
    print(get_exchange_data(key))


if __name__ == '__main__':
    main()













