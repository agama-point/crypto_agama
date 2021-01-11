# agama_point - crypto21
# https://wolovim.medium.com/ethereum-201-hd-wallets-11d0c93c87f7
# generate, to_seed, to_hd_master_key(seed), to_mnemonic

from mnemonic import Mnemonic
from crypto_agama.transform import *
import base58

TW = 80 # terminal width

mnemo = Mnemonic("english")

print("-"*TW)
print("agama_point - crypto21 - Bitcoin test")
print("-"*TW)
##words = mnemo.generate(strength=128) # 128-256 (12/24)
words_book = "army van defense carry jealous true garbage claim echo media make crunch"
words_tbtc = "major easy ignore body rule stay gorilla eager arch actor scan thank"
words_test = "employ blouse total detect move attitude trophy space crystal size green naive"

words = words_tbtc
print(words)

#seed = mnemo.to_seed(words, passphrase="SuperDuperSecret")
seed_bytes = mnemo.to_seed(words, passphrase="")
print("mnemo.to_seed = seed_bytes: ", seed_bytes)

xprv = mnemo.to_hd_master_key(seed_bytes)
print("mnemo.to_hd_master_key = xprv: ", xprv) 

##print(mnemo.to_mnemonic(hdmk))

entropy = mnemo.to_entropy(words)
print("entropy: ", entropy)

print("-"*TW)

"""
bin = hexToBin(seed)
print("bin", bin)

num = seed

privateKey = numToWIF(num,"EF")
print("privateKey: ",privateKey)
"""

import binascii, hmac, hashlib
# the HMAC-SHA512 `key` and `data` must be bytes:
##binascii.unhexlify(seed)

I = hmac.new(b'Bitcoin seed', seed_bytes, hashlib.sha512).digest()
L, R = I[:32], I[32:]
master_private_key = int.from_bytes(L, 'big')
master_chain_code = R


VERSION_BYTES = {
   'mainnet_public': binascii.unhexlify('0488b21e'), 'mainnet_private': binascii.unhexlify('0488ade4'),
   'testnet_public': binascii.unhexlify('043587cf'), 'testnet_private': binascii.unhexlify('04358394'),
}

version_BYTES = "mainnet_private"
print("version_BYTES: ", version_BYTES)

version_bytes = VERSION_BYTES[version_BYTES] #  testnet_public
depth_byte = b'\x00'
parent_fingerprint = b'\x00' * 4
child_number_bytes = b'\x00' * 4
key_bytes = b'\x00' + L
all_parts = (
    version_bytes,      # 4 bytes  
    depth_byte,         # 1 byte
    parent_fingerprint,  # 4 bytes
    child_number_bytes, # 4 bytes
    master_chain_code,  # 32 bytes
    key_bytes,          # 33 bytes
)
all_bytes = b''.join(all_parts)
root_key = base58.b58encode_check(all_bytes).decode('utf8')
print("root_key: ", root_key)

print("root_www: ", "xprv9s21ZrQH143K3Lkdp2LWERaQjMDcGfCLLVrB3QsKmxNPqrwAcGimMY8c3p95mwDieoNAE19rKNqH3FnhiEBFxUa2RWUThPxYjdQ64HQ82Lw")
# xprv9s21ZrQH143K...T2emdEXVYsCzC2U

print("-"*TW)

"""
from ecdsa import SECP256k1
from ecdsa.ecdsa import Public_key
SECP256k1_GEN = SECP256k1.generator
def serialize_curve_point(p):
   x, y = K.x(), K.y()
   if y & 1:
      return b'\x03' + x.to_bytes(32, 'big')
   else:
      return b'\x02' + x.to_bytes(32, 'big')
    
def curve_point_from_int(k):
   return Public_key(SECP256k1_GEN, SECP256k1_GEN * k).point

def fingerprint_from_private_key(k):
   K = curve_point_from_int(k)
   K_compressed = serialize_curve_point(K)
   identifier = hashlib.new(
      'ripemd160',
      hashlib.sha256(K_compressed).digest(),
   ).digest()
   return identifier[:4]

depth = 0
parent_fingerprint = None
child_number = None
private_key = master_private_key
chain_code = master_chain_code

p = curve_point_from_int(private_key)
public_key_bytes = serialize_curve_point(p)
print(f'public key: 0x{public_key_bytes.hex()}')
"""

print("-"*TW)
print("cryptos")
print("-"*TW)


# https://github.com/primal100/pybitcointools
from cryptos import * # pip install wheel, pbkdf2, cryptos
#words = entropy_to_words(os.urandom(16))

print("wodrs checkum-valid: ", keystore.bip39_is_checksum_valid(words))

"""
c = Bitcoin(testnet=True)
priv = sha256(words)
print("priv:", priv)

pub = c.privtopub(priv)
print("pub:", pub)

addr = c.pubtoaddr(pub)
print("addr:", addr)

print("-"*TW)

#inputs = c.unspent(addr)
#print("inputs:", inputs)
"""

coin = Bitcoin(testnet=True)
wallet = coin.wallet(words)
print("wallet: ", wallet)
der = wallet.keystore.root_derivation # "m/44'/0'/0'"
print("root_derivation: ", der)

xprv = wallet.keystore.xprv
print("xprv: ", xprv)

xpub = wallet.keystore.xpub
print("xpub: ", xpub)

addr1 = wallet.new_receiving_address()
print("addr1: ", addr1)

wpk1 = wallet.privkey(addr1)
print("wallet.privkey: ", wpk1)

print("-"*TW)
addr2 = wallet.new_change_address()
print("addr2: ", addr2)


print("ok")
