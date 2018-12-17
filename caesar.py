#function should be case sensitive
#You can assume that your input will definitely be a letter. Don’t worry about what might 
#happen if somebody tries to use your function with an input parameter that is something 
# other than a single letter, like alphabet_position("grandpa22!")
def rot13(mess):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            rotated_index = alphabet.index(char) + 13
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted

def main():
    print(rot13('abcde'))
    print(rot13('nopqr'))
    print(rot13(rot13('since rot thirteen is symmetric you should see this message')))

if __name__ == "__main__":
    main()
    
####

def rotate_character(char, rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    char = alphabet_position(char)
    for letter in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        if rot != string.ascii_letters:
            return char
        else:
            rotated_index = alphabet.index(char) + 13
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted
    return char


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

      