
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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



