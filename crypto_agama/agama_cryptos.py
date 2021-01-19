from cryptos import * # pip install wheel, pbkdf2, cryptos
from mnemonic import Mnemonic
from crypto_agama.transform import create_root_key


def create_wallet(words, c="tBTC", wnum = 0, debug=True): # tBTC/BTC/LTC

    mnemo = Mnemonic("english")
    #seed = mnemo.to_seed(words, passphrase="SuperDuperSecret")
    seed_bytes = mnemo.to_seed(words, passphrase="")

    xprv = mnemo.to_hd_master_key(seed_bytes)
    entropy = mnemo.to_entropy(words)

    if (c=="LTC"): coin = Litecoin(testnet=False)
    if (c=="BTC"): coin = Bitcoin(testnet=False)
    if (c=="tBTC"): coin = Bitcoin(testnet=True)

    wallet = coin.wallet(words)

    xprv = wallet.keystore.xprv
    xpub = wallet.keystore.xpub

    addr = wallet.new_receiving_address()
    wpk = wallet.privkey(addr)

    if wnum == 1:
      addr = wallet.new_change_address()
      wpk = wallet.privkey(addr)

    if wnum == 2:
      addr = wallet.new_change_address()
      addr = wallet.new_change_address()
      wpk = wallet.privkey(addr)

    deriv = wallet.keystore.root_derivation # "m/44'/0'/0'"

    return addr, wpk, deriv, xprv, entropy
