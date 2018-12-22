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
