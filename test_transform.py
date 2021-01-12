from crypto_agama.transform import *

num = 123456789012345678901 # 21)
# num = 1024 # 21)

print("_______num: ", num)

hexFromNum = num_to_hex(num)
print("hexFromNum: ", hexFromNum)


numFromHex = hex_to_num(hexFromNum)
print("numFromHex: ", numFromHex)


binFromHex = hex_to_bin(hexFromNum)
print("binFromHex: ", binFromHex)

binFromNum = num_to_bin(num)
print("binFromNum: ", binFromNum)


print("-"*63)


print("num: ", num)

wif = num_to_wif(num)
print("wif: ", wif)

numwif = wif_to_num(wif)
print("num_wif: ", numwif)

num58 = convert_to_base58(num)
print("num58: ", num58)

print("-"*63)

str_txt = "ABCDEFGHIJKLMNOPQR123"
print("str_txt: ", str_txt)

bin1 = str_to_bin(str_txt)
print("bin1: ", bin1)

bin = "1010101010111111000001110001"
print("bin_str: ", bin)


print("-"*63)




"""
binToHex

bin8tohex

binToStr
"""