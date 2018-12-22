#function should be case sensitive
#You can assume that your input will definitely be a letter. Don’t worry about what might 
#happen if somebody tries to use your function with an input parameter that is something 
# other than a single letter, like alphabet_position("grandpa22!")
    
####
#      use alphabet_position maybe
#      preserve case
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


def encrypt(text, rot):
    encrypted = ''
    for char in text:
        encrypted = encrypted + rotate_character(char, rot)
    return encrypted


        
        
def main():
    text = input("Type a message:")
    rot = int(input("Rotate by:"))
    print(encrypt(text, rot))

          
if __name__ == "__main__":
          main()
