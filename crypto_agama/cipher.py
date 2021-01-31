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



""" polybius code - basic an simple way:
- 1 2 3 4 5
1 A B C D E
2 F G H I K
3 L M N O P
4 Q R S T U
5 V W X Y Z
"""
p1 = {
"A": "11", "B": "12", "C": "13", "D": "14", "E": "15",
"F": "21", "G": "22", "H": "23", "I": "24", "K": "25",
"L": "31", "M": "32", "N": "33", "O": "34", "P": "35",
"Q": "41", "R": "42", "S": "43", "T": "44", "U": "45",
"V": "51", "W": "52", "X": "53", "Y": "54", "Z": "55"
}

def polybius_decrypt(text, p=p1):
   polyb = ""
   for ch in text:
      try:
         _i = ch.upper()
         _pi = p[_i]
         # print(ch, _pi)
         polyb += _pi + " "
      except:
         print("polybios_decrypt.Err")
   return polyb


# function to display polybius cipher text 
def polybius_cipher(s): 
   for char in s:

      row = int((ord(char) - ord('a')) / 5) + 1 # finding row of the table
      col = ((ord(char) - ord('a')) % 5) + 1 # finding column of the table
      if char == 'k': 
            row = row - 1
            col = 5 - col + 1
      # if character is greater than 'j' 
      elif ord(char) >= ord('j'): 
            if col == 1 : 
                  col = 6
                  row = row - 1
            col = col - 1
      print(row, col, end ='', sep ='')
