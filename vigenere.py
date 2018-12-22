import string
from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    encrypted = ''
    counter = 0
    i = 0
    for letter in text:
        if letter.isalpha():
            i = alphabet_position(key[counter])
            encrypted = encrypted + rotate_character(letter, i)
            counter = ((counter + 1) % len(key))
        else:
            encrypted = encrypted + letter
    return encrypted

def main():
    text = input("Type a message: ")
    print(text)
    key = input("Encryption key: ")
    print(key)
    print(encrypt(text, key))
          
if __name__ == "__main__":
          main()