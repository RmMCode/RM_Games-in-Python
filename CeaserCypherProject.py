def encrypt(message, shift):
    cipher = ''
    for char in message: 
        if char == ' ':
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

def decrypt(message, shift):
    cipher = ''
    for char in message:
        if char == ' ':
           cipher = cipher + char
        elif char.isupper():
           cipher = cipher + chr((ord(char) - shift - 65) % 26 + 65)
        else:
           cipher = cipher + chr((ord(char) - shift - 97) % 26 + 97)
    return cipher

#Main Program
option = int(input("Enter 1 to encrypt, 2 to decrypt, 3 to quit: "))

while option != 3:
    if option == 1:
        message = str(input("Enter a message to encrypt: "))
        shift = int(input("Enter shift or rotation: "))
        print("Original Message: ", message)
        print("After encryption: ", encrypt(message, shift))
    elif option == 2:
        message = str(input("Enter a message to decrypt: "))
        word    = str(input("Enter a word in the string: "))
        msg_found = False
        for shift in range(0,26):
            dec_msg = decrypt(message, shift)
            if word in dec_msg:
                print("Original Message: ", message)
                print("The rotation was: ", shift)
                print("After decryption: ", dec_msg)
                msg_found = True
                break        
        if msg_found == False:
            print("Message could not be decoded")
    else:
        print("Not a valid input")
    
    option = int(input("Enter 1 to encrypt, 2 to decrypt, 3 to quit: "))
