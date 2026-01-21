#generate an encrypted message for the user input. Replace each character with random character from a set of special characters.

import random
import string

chars = string.ascii_letters + string.digits + string.punctuation + " "#all possible characters excluding space
chars = list(chars) #converting to list for easy access
key = chars.copy() #copying the original list to create a key for encryption
random.shuffle(key) #shuffling the key list to create a random mapping

#ENCRYPTION
plain_txt = input("Enter the message to encrypt: ")
cipher_txt = ""
for letter in plain_txt:
    index = chars.index(letter) #finding the index of the letter in original list
    cipher_txt += key[index] #getting the corresponding character from the shuffled list using the index

print("Original Message : ", plain_txt)
print("Encrypted Message: ", cipher_txt)

#DECRYPTION
cipher_txt = input("Enter the message to decrypt: ")
plain_txt = ""
for letter in cipher_txt:
    index = key.index(letter) #finding the index of the letter in key list
    plain_txt += chars[index] #getting the corresponding character from the original list

print("Encrypted Message: ", cipher_txt)
print("Original Message : ", plain_txt)