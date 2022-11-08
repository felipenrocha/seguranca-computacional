from caesar import cesar_encode, cesar_decode, alfabeto


def key_gen(key, message):
    """Function to generate key repeating the base key until it has the size of the message"""
    size_of_key = len(key)
    new_key = ''
    for index, letter in enumerate(message):
        new_key += key[index % size_of_key]
    return new_key

def encryption(key, message):
    """Function to encrypt the key using caesar cipher"""
    criptogram = ''
    key = key_gen(key, message)
    for index, letter in enumerate(message):
        # get key index to use it as the key in caesar cipher with the letter
        key_index = alfabeto.find(key[index])
        new_key = cesar_encode(letter, key_index)
        criptogram += new_key
    return criptogram


def decryption(key, criptogram):
    message = ''
    key = key_gen(key, criptogram)
    for index, letter in enumerate(criptogram):
        # get key index to use it as the key in caesar cipher with the letter
        key_index = alfabeto.find(key[index])
        new_key = cesar_decode(letter, key_index)
        message += new_key
    return message

