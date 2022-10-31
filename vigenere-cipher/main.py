from vigenere import generate_key, encrypt, decrypt
def main():
    message = 'ATACARBASESUL'
    key = generate_key('LIMAO', message)
    print('Message: ', message)
    print('Key: ', key)
    criptogram = encrypt(key, 'ATACARBASESUL')
    print('Encrypted: ', criptogram)
    decrypted = decrypt(key, criptogram)
    print('Decrypted: ', decrypted)
    return
if __name__ == "__main__":
    main()