# blockchain and mempool api - bitcoin / bitcoin tes
# agama_point 2021/01

import requests, json

url_btcusd = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"
url_btct = "https://chain.so/api/v2/get_tx_received/BTCTEST/$addrBTCT"
url_mempool_fees = "https://mempool.space/api/v1/fees/recommended"


# note: 10-20 sec. pause is required
def bitcoin_usd():
    res = requests.get(url_btcusd)
    # print(res)
    btcusd = res.json()['quotes']["USD"]["price"]
    return float(btcusd)


def btc_mempool_fees():
    res = requests.get(url_mempool_fees)
    print(res)
    res_json =  res.json()
    fastestFee = res_json['fastestFee']
    halfHourFee = res_json['halfHourFee']
    hourFee = res_json['hourFee']
    return fastestFee, halfHourFee, hourFee


def btct_info():
    import requests, json
    res = requests.get(url_btct)
    print(res)
    btcti = res.json()['quotes']["USD"]["price"]
    return float(btcti)
