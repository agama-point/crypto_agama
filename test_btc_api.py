from crypto_agama.btc_api import bitcoin_usd, btc_mempool_fees

print("bitcoin - coinpaprika_api")
btcusd = bitcoin_usd()
print(btcusd)

print("-"*39)

btc_fee = btc_mempool_fees()
print("btc_fee",btc_fee," sat/B")


print("ok")