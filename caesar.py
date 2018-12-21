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
    low_letter = letter.lower() 
    for char in low_letter:
        if char == ' ':
            letter_pos = letter_pos + ' '
        else:
            letter_pos = alphabet.index(char)
    
    return letter_pos


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


        
        
def main():
    print(rotate_character('A', 26))
          
if __name__ == "__main__":
          main()
