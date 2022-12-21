
import string

def key_gen(key, message):
    """Function responsble to generate key repeating the base key until it has the size of the message"""
    size_of_key = len(key)
    new_key = ''
    for index, letter in enumerate(message):
        new_key += key[index % size_of_key]
    return new_key


def encryption(key, message):
    """Function to encrypt message based o Vigenere Cipher using key
    """

    # generate key
    key = key_gen(key, message)
    # set new string
    criptogram = ''
    # index used to encrypt (only increased when a char is pushed)
    key_index = 0

    #loop through string
    for i in range(len(message)):
        # if message is an alphabet character encrypt using equation and push to final string
        if message[i].isalpha():
          
            x = (ord(message[i]) +
                ord(key[key_index])) % 26   # ord returns the unicode int of character
            x += ord('A')
            criptogram += chr(x)
            key_index += 1
        else:
        # else just push the other characters
            criptogram += message[i]
    return criptogram
     


def decryption(key, criptogram):
    """Function to decrypt message based o Vigenere Cipher using key"""
    # generate key
    key= key_gen(key, criptogram)

    # set all characters to upper to normalize string
    criptogram = criptogram.upper()
    # set new string
    message = ''

    # index used to decrypt (only increased when a char is pushed)
    key_index = 0

    # loop through message
    for i in range(len(criptogram)):
        #check if its an alphabet character 
        if criptogram[i].isalpha():
            x = (ord(criptogram[i]) -
                ord(key[key_index]) + 26) % 26
            x += ord('A')
            message += chr(x)
            key_index += 1
        else:
            message += criptogram[i]
    return message 


