#function should be case sensitive
#You can assume that your input will definitely be a letter. Don’t worry about what might 
#happen if somebody tries to use your function with an input parameter that is something 
# other than a single letter, like alphabet_position("grandpa22!")
import string
    
####
#      use alphabet_position maybe
#      preserve case

def rotate_character(char, rot)
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    #char = alphabet_position

    #while statement, isalpha
    #if character is upper he did index =

    while char.isalpha:
#        char = alphabet_position(char)
        if char.isupper == True:
            return char

        if char.islower == True:
            return char
    
    
    

    return rotated 


####

def alphabet_position(letter):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    low_letter = letter.lower() 
    for char in low_letter:
        if char == ' ':
            letter_pos = letter_pos + ' '
        else:
            letter_pos = alphabet.index(char)
    
    return letter_pos

#def rotate_character(char, rot):

    

def main():
    print(alphabet_position('Z'))



if __name__ == "__main__":
    main()

      