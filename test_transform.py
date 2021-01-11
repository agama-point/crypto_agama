from crypto_agama.transform import *

num = 123456789012345678901 # 21)
num = 10 # 21)


print("num: ", num)

wif = numToWIF(num)
print("wif: ", wif)

numwif = WIFToNum(wif)
print("num_wif: ", numwif)

num58 = convertToBase58(num)
print("num58: ", num58)

print("-"*63)

str_txt = "ABCDEFGHIJKLMNOPQR123"
print("str_txt: ", str_txt)

bin1 = str2bin(str_txt)
print("bin1: ", bin1)

bin = "1010101010111111000001110001"
print("bin_str: ", bin)

#s2b = strToBin(bin)
#print("bin: ", s2b)

hexFromNum = numToHex(num)
print("hexFromNum: ", hexFromNum)


numFromHex = hexToNum(hexFromNum)
print("numFromHex: ", numFromHex)


binFromHex = hexToBin(hexFromNum)
print("binFromHex: ", binFromHex)


"""
binToHex

bin8tohex

binToStr
"""