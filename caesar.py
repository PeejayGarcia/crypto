#function should be case sensitive
#You can assume that your input will definitely be a letter. Don’t worry about what might 
#happen if somebody tries to use your function with an input parameter that is something 
# other than a single letter, like alphabet_position("grandpa22!")
def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    low_letter = letter.lower()
    letter_pos = ord(low_letter)
    
    return letter_pos

def main():
    print(alphabet_position('b'))


if __name__ == "__main__":
    main()