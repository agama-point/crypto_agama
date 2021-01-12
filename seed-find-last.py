#!/usr/bin/env python
# -*- coding: utf-8 -*-

# agama_point: find last word from seed (around 128 validated)

from crypto_agama.transform import seedWords
from cryptos import * # pip install wheel, pbkdf2, cryptos

bip39 = seedWords()

words_book = "army van defense carry jealous true garbage claim echo media make crunch"
words_tbtc = "major easy ignore body rule stay gorilla eager arch actor scan thank"
words_test = "employ blouse total detect move attitude trophy space crystal size green naive"

words_test11 = "major easy ignore body rule stay gorilla eager arch actor scan "

print("-"*30)

num = 0
for word in bip39:
    words = words_test11 + word
   
    if (keystore.bip39_is_checksum_valid(words)[0]):
        print(num, "wodrs checkum-valid: ", word, keystore.bip39_is_checksum_valid(words))
        num += 1
