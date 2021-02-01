# on-line - converter:
# https://iancoleman.io/bip39/#english
# 2021-02-01

from mnemonic import Mnemonic
from crypto_agama.transform import *
from crypto_agama.seed_tools import *
from crypto_agama.agama_cryptos import create_wallet
import base58

TW = 80 # terminal width

print("-"*TW)
print("agama_point - test_converter.py - iancoleman.io/bip39")
print("-"*TW)

mnemo = Mnemonic("english")
print("Mnemonic Language: english")

##words = mnemo.generate(strength=128) # 128-256 (12/24)
words = "army van defense carry jealous true garbage claim echo media make crunch"
#passphrase = "test"
passphrase = ""

print("BIP39 Mnemonic: ", words)

print("-"*TW)
print("--- BIP39 Seed ---") 

print("BIP39 Passphrase (optional): ", passphrase)
seed_bytes = mnemo.to_seed(words, passphrase=passphrase)
#seed_bytes = mnemo.to_seed(words, passphrase="")
# print("mnemo.to_seed = seed_bytes: ", seed_bytes)

print(seed_bytes.hex()) # hexadecimal_string = some_bytes.hex()
print()

print("--- BIP32 Root Key ---")
root_key = create_root_key(seed_bytes)
print("create_root_key(): ", root_key)

xprv = mnemo.to_hd_master_key(seed_bytes)
print("to_hd_master_key:  ", xprv) 

print("-"*TW)
print()
##print(mnemo.to_mnemonic(hdmk))

entropy = mnemo.to_entropy(words)
print("entropy: ", entropy)

print("-"*TW)
print("-"*TW)
print()
print("Derivation Path")
print("BIP32 | BIP44 | BIP49 | BIP84 | BIP141")


#def create_wallet(words, passphrase="", c="tBTC", wnum = 0, debug=True): # tBTC/BTC/LTC

w = create_wallet(words, passphrase=passphrase, c="BTC")
wcoin, pcoin = w[0],  w[1]
print("wallet-priv: ", pcoin)
print("wallet-pub:  ", wcoin)
print(w[2])

print("---")
w = create_wallet(words, passphrase=passphrase, c="BTC",wnum=1)
wcoin, pcoin = w[0],  w[1]
print("wallet-priv: ", pcoin)
print("wallet-pub:  ", wcoin)
print(w[2])

print("ok")