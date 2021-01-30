#!/usr/bin/env python
# -*- coding: utf-8 -*-
# crypto_agama.transform 2016-21

import hashlib, binascii
from hashlib import sha256
# import ecdsa

DEBUG = True

"""
num_to_hex(255)    # '0xff'
hex_to_num('0xff') # 255
num_to_bin(123)    # '0b1111011'
num_to_bin(123, True) # '1111011' # to string
hex_to_bin('0xff') # '0b11111111'
bin_to_hex('0b11111111') # '0xff'
str_to_hex("abc")  # '616263' # ASCII
str_to_bin("abc")  #'110000111000101100011'
bin_to_str('110000111000101100011') # x?  b'\x18qc'
bin8_to_hex?
bin_to_str?
int_to_bytes?

short_str("abcdefghijklmnopqrtsuvwxyz")    # 'abcdefghijkl...opqrtsuvwxyz'
short_str("abcdefghijklmnopqrtsuvwxyz",3)  # 'abc...xyz'
text_to_bits("abc")                        # '011000010110001001100011'
text_from_bits('011000010110001001100011') # 'abc'

hash_sha256_str("agama") # '52589fac98630c603bd5c2b08cb0f6ccf273cc4a4772f0ff28d49a01bc7d2f4b'

hashhex = hash_sha256_str("agama")
hashnum = int(hashhex, 16)
convert_to_base58(hashnum) # '6YSp1VMaYGo5enJRFFwhhcNmrhGWPmJgSZqiS2sv3fwQ'

num_to_wif 
wif_to_num 
is_valid_wif
seed_words 
num_to_address

"""

BASE_58_CHARS = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
BASE_58_CHARS_LEN = len(BASE_58_CHARS)

MAINNET_PREFIX = '80'
TESTNET_PREFIX = 'EF'


def hash_sha256_str(string):
    """
    Return a SHA-256 hash of the given string
    """
    return sha256(string.encode('utf-8')).hexdigest()


def convert_to_base58(num):
    sb = ''

    while (num > 0):
        r = num % 58   # divide by 58 and gives the remainder
        sb = sb + BASE_58_CHARS[r]
        num = num // 58
    return sb[::-1]


def num_to_wif(numPriv,prefix=MAINNET_PREFIX,leading="1",debug=DEBUG):
  # base58.b58encode_check(bytes).decode('utf8')
  privKeyHex = prefix+hex(numPriv)[2:].strip('L').zfill(64)
  privKeySHA256Hash = sha256(binascii.unhexlify(privKeyHex)).hexdigest()
  privKeyDoubleSHA256Hash = sha256(binascii.unhexlify(privKeySHA256Hash)).hexdigest()
  checksum = privKeyDoubleSHA256Hash[:8]
  wifNum = int(privKeyHex + checksum, 16)
  if debug: print("DEBUG-wifNum: ", wifNum)
  wifNum58 = convert_to_base58(wifNum)
  if debug: print("DEBUG-wifNum58: ", wifNum58)
  return leading + wifNum58


def wif_to_num(wifPriv):
    numPriv = 0
    for i in range(len(wifPriv)):
      numPriv += BASE_58_CHARS.index(wifPriv[::-1][i])*(BASE_58_CHARS_LEN**i)

    numPriv = numPriv/(2**32)%(2**256)
    return numPriv


def num_to_hex(num):
   # ret = num.to_bytes(((integer.bit_length() + 7) // 8),"big").hex()
   ret = hex(num)
   return ret


def hex_to_num(hex):
  return int(hex, 16)


def hex_to_bin(hexn, to_string = False):
  #bin(private_key1.to_bin())
  _bin = bin(int(hexn, base=16))
  if to_string:
    return str(_bin)[2:]
  else:
    return _bin


def num_to_bin(num, to_string = False):
  _bin = bin(int(num))
  if to_string:
    return str(_bin)[2:]
  else:
    return _bin


def bin_to_hex(binx):
   return hex(int(binx, 2))


def bin8_to_hex(strh):	
   tB = []
   tBs ="0x"	
   #print("len:"+str(len(strh)))
   try:
     for ib in range (0,160):
       Bapp = binToHex("0b"+str(strh)[2+ib*8:2+ib*8+8])	 
       tB.append(Bapp)
       print(Bapp,end="")
       tBs = tBs+tB[ib][2:4]
       #print ib,tB[ib]
   except: 
     err=True
     print(ib,end="")

   return tBs


def str_to_hex(str_txt):
  s = str_txt.encode('utf-8')
  return s.hex()


def str_to_bin(str_txt):
  # res = bin(reduce(lambda x, y: 256*x+y, (ord(c) for c in str), 0))
  res = ''.join(format(ord(i), 'b') for i in str_txt)
  return res


def bin_to_str(bin):
  n = int(bin, 2)
  return binascii.unhexlify('%x' % n)


def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int_to_bytes(n).decode(encoding, errors)


def int_to_bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1))) 


def short_str(s,l=12):
  return str(s[:l])+"..."+str(s[-l:])


# ------------------------ hexdump -------------------------
def group(a, *ns):
  for n in ns:
    a = [a[i:i+n] for i in range(0, len(a), n)]
  return a


def join(a, *cs):
  return [cs[0].join(join(t, *cs[1:])) for t in a] if cs else a


def hexdump(data):
  toHex = lambda c: '{:02X}'.format(c)
  toChr = lambda c: chr(c) if 32 <= c < 127 else '.'
  make = lambda f, *cs: join(group(list(map(f, data)), 8, 2), *cs)
  hs = make(toHex, '  ', ' ')
  cs = make(toChr, ' ', '')
  for i, (h, c) in enumerate(zip(hs, cs)):
    print ('{:010X}: {:48}  {:16}'.format(i * 16, h, c))


# ------------------------ crypto --------------------------
def seed_words():
    from crypto_agama.seed_english_words import english_words_bip39
    return english_words_bip39.split(",")


def is_valid_wif(wifPriv):
  return numToWIF(WIFToNum(wifPriv)) == wifPriv


def num_to_address(numPriv):
    pko = ecdsa.SigningKey.from_secret_exponent(numPriv, CURVE_TYPE)
    pubkey = binascii.hexlify(pko.get_verifying_key().to_string())
    pubkeySHA256Hash = sha256(binascii.unhexlify('04' + pubkey)).hexdigest()
    pubkeySHA256RIPEMD160Hash = hashlib.new('ripemd160', binascii.unhexlify(pubkeySHA256Hash)).hexdigest()

    hash1 = sha256(binascii.unhexlify('00' + pubkeySHA256RIPEMD160Hash)).hexdigest()
    hash2 = sha256(binascii.unhexlify(hash1)).hexdigest()
    checksum = hash2[:8]

    encodedPubKeyHex = pubkeySHA256RIPEMD160Hash + checksum
    encodedPubKeyNum = int(encodedPubKeyHex, 16)

    base58CharIndexList = []
    while encodedPubKeyNum != 0:
      base58CharIndexList.append(encodedPubKeyNum % BASE_58_CHARS_LEN)
      encodedPubKeyNum /= BASE_58_CHARS_LEN

    m = 0
    while encodedPubKeyHex[0 + m : 2 + m] == '00':
        base58CharIndexList.append(0)
        m = m + 2

    address = ''
    for i in base58CharIndexList:
      address = BASE_58_CHARS[i] + address

    return '1' + address


def ent_to_phrase(entropy): 
    #tests to see if provided entropy produces desired word list
    hashes = HashingFunctions()
    hashes.get_input(entropy)
    hashes.create_check_sum()
    hashes.create_word_list()
    phrase = hashes.result_word_list
    return phrase


def phrase_to_key(phrase): 
    #tests to see if word list converts to desired master key
    hashes = HashingFunctions(None, phrase)
    hashes.create_binary_seed()
    return hashes.binary_seed


def create_root_key(seed_bytes,version_BYTES = "mainnet_private"):
   import binascii, hmac, hashlib, base58
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

   print("version_BYTES: ", version_BYTES)

   version_bytes = VERSION_BYTES[version_BYTES] #  testnet_public
   depth_byte = b'\x00'
   parent_fingerprint = b'\x00' * 4
   child_number_bytes = b'\x00' * 4
   key_bytes = b'\x00' + L
   all_parts = (
      version_bytes,       #  4 bytes  
      depth_byte,          #  1 byte
      parent_fingerprint,  #  4 bytes
      child_number_bytes,  #  4 bytes
      master_chain_code,   # 32 bytes
      key_bytes,           # 33 bytes
   )
   all_bytes = b''.join(all_parts)
   root_key = base58.b58encode_check(all_bytes).decode('utf8')
   return root_key
