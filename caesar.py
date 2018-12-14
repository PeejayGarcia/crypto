#function should be case sensitive
#You can assume that your input will definitely be a letter. Don’t worry about what might 
#happen if somebody tries to use your function with an input parameter that is something 
# other than a single letter, like alphabet_position("grandpa22!")
def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter = letter.lower()
    
    return letter

def main():
    print(alphabet_position('aBa'))


if __name__ == "__main__":
    main()