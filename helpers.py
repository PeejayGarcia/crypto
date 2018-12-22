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