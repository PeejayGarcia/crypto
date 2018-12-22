import string


def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    while letter.isalpha():
        if letter.isupper():
            lower = letter.lower()
            letter_pos = alphabet.index(lower)
            return letter_pos
        if letter == ' ':
            letter_pos = letter_pos + ' '
            return letter_pos
        else:
            letter_pos = alphabet.index(letter)
            return letter_pos
    return letter


def rotate_character(char, rot):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase

    while char.isalpha():
        if char.isupper():
            position = ((upper.find(char) + rot) % 26)
            new_position = upper[position]
            return new_position
        else:
            position = ((lower.find(char)  + rot) % 26)
            new_position = lower[position]
            return new_position  
    return char


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