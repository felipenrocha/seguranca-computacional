
import string
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def key_gen(key, message):
    """Function to generate key repeating the base key until it has the size of the message"""
    size_of_key = len(key)
    new_key = ''
    for index, letter in enumerate(message):
        new_key += key[index % size_of_key]
    return new_key


def encryption(key, message):
    key = key_gen(key, message)
    criptogram = ''
    for i in range(len(message)):
        if message[i].isalpha():
            x = (ord(message[i]) +
                ord(key[i])) % 26
            x += ord('A')
            criptogram += chr(x)
        else:
            criptogram += message[i]
    return criptogram
     


def decryption(key, criptogram):
    key= key_gen(key, criptogram)
    criptogram = criptogram.upper()
    message = ''
    key_index = 0
    for i in range(len(criptogram)):
        if criptogram[i].isalpha():
            x = (ord(criptogram[i]) -
                ord(key[key_index]) + 26) % 26
            x += ord('A')
            message += chr(x)
            key_index += 1
        else:
            message += criptogram[i]
    return message 


def cesar_encode(message, key):
    message_encoded = ''
    for letra in message:
        letter_index = alfabeto.find(letra)
        new_letter = alfabeto[((letter_index + key) % 26)]
        message_encoded += new_letter 
    return message_encoded

def cesar_decode(message, key):
    message_decoded = ''
    for letra in message:
        letter_index = alfabeto.find(letra)
        new_letter = alfabeto[((letter_index - key) % 26)]
        message_decoded += new_letter 
    return message_decoded

