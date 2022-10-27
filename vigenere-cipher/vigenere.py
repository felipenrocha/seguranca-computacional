alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    key = generate_key('LIMAO', 'ATACARBASESUL')
    criptogram = encode(key, 'ATACARBASESUL')
    print(key)

def generate_key(key, message):
    """Function to generate key repeating the base key until it has the size of the message"""
    size_of_key = len(key)
    new_key = ''
    for index, letter in enumerate(message):
        new_key += key[index % size_of_key]
    return new_key

def encode(key, message):
    criptogram = ''
    for index, letter in enumerate(message):
        criptogram += ''

if __name__ == "__main__":
    main()