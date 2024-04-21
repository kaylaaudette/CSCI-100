# Kayla Audette

import math
# This prints out the ASCII for each character in the string  
m = "This is a message."
for i in range(len(m)):
    print( ord(m[i]) )
    
# Question 3
def decrypt(x):
    by2 = len(x) // 2
    odd = x[:by2]
    even = x[by2:]
    plaintext = ' '
    for i in range(by2):
        plaintext = plaintext + even[i]
        plaintext = plaintext + odd[i]
        if len(odd) < len(even):
            plaintext = plaintext + even[-1] 
            print(plaintext)

# Question 4
def substitutionEncrypt(plainText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    plainText = plainText.lower()
    cipherText = ""
    for ch in plainText:
        idx = alphabet.find(ch)
        cipherText = cipherText + key[idx]
    return cipherText
   
def substitutiondecrypt(cipherText, key):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipherText = cipherText.lower()
    plainText = ""
    for ch in cipherText:
        idx = alphabet.find(ch)
        plainText = plainText + key [idx]
    return plainText
   
key = 'zyxwvutsrqponmlkjihgfedcba '
plainText = 'the quick brown fox'

print("------------------Q3-------------------")
decrypt("o r ue wsmyuaespraeoe")   
print("------------------Q4-------------------")
encryptMsg = substitutionEncrypt(plainText,key)
print( "Encrypted message: " + encryptMsg )
decrypt1 = substitutiondecrypt(encryptMsg, key)
print("Decrypted message: " + decrypt1)
print("---------------------------------------")