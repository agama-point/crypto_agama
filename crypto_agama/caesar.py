# 
# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm

"""
print "Plain Text : " + text
print "Shift pattern : " + str(s)
print "Cipher: " + caesar_encrypt(text,s)
"""


def caesar_encrypt(text,s,up=True):
   result = ""

   for i in range(len(text)):
      char = text[i]
      # Encrypt uppercase characters in plain text
      
      if (char.isupper() or (ord(char) == 32)):
         if(ord(char) == 32):
            result += " "
         else:
            result += chr((ord(char) + s-65) % 26 + 65)
      # Encrypt lowercase characters in plain text
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
   if (up): 
      result = result.upper()
   
   return result
