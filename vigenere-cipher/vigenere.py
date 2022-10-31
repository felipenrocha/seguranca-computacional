from caesar import cesar_encode, cesar_decode, alfabeto


def generate_key(key, message):
    """Function to generate key repeating the base key until it has the size of the message"""
    size_of_key = len(key)
    new_key = ''
    for index, letter in enumerate(message):
        new_key += key[index % size_of_key]
    return new_key

def encrypt(key, message):
    """Function to encrypt the key using caesar cipher"""
    criptogram = ''
    for index, letter in enumerate(message):
        # get key index to use it as the key in caesar cipher with the letter
        key_index = alfabeto.find(key[index])
        new_key = cesar_encode(letter, key_index)
        criptogram += new_key
    return criptogram


def decrypt(key, criptogram):
    message = ''
    for index, letter in enumerate(criptogram):
        # get key index to use it as the key in caesar cipher with the letter
        key_index = alfabeto.find(key[index])
        new_key = cesar_decode(letter, key_index)
        message += new_key
    return message

