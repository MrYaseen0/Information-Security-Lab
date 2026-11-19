import random
import string

def make_key():
    letters = list(string.ascii_lowercase)
    random.shuffle(letters)
    return "".join(letters)

def encrypt(text, key):
    table = str.maketrans(string.ascii_lowercase + string.ascii_uppercase, key + key.upper())
    return text.translate(table)

def decrypt(text, key):
    table = str.maketrans(key + key.upper(), string.ascii_lowercase + string.ascii_uppercase)
    return text.translate(table)

key = "qwertyuiopasdfghjklzxcvbnm"  # or use make_key() for a random one
message = "Hello, World!"

encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)

print(encrypted)
print(decrypted)

# ----

def ceasar (text,shift):
  result = ""
  for ch in text:
    if ch.isalpha():
      base = ord('A') if ch.isupper() else ord ('a')
      result+= chr((ord(ch) - base + shift) % 26 + base)
    else:
      result += ch
  return result

message = "Yaseen khan 778 +"
encrypted = ceasar(message, 3)
decrypted = ceasar(encrypted, -3)

print(encrypted)
print(decrypted)