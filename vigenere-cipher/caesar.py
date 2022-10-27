
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def cesar_encode(mensagem, chave):
    mensagem_encoded = ''
    for letra in mensagem:
        letter_index = alfabeto.find(letra)
        new_letter = alfabeto[((letter_index + chave) % 26)]
        mensagem_encoded += new_letter 
    return mensagem_encoded

def cesar_decode(mensagem, chave):
    mensagem_decoded = ''
    for letra in mensagem:
        letter_index = alfabeto.find(letra)
        new_letter = alfabeto[((letter_index - chave) % 26)]
        mensagem_decoded += new_letter 
    return mensagem_decoded





def main():
    print("Welcome to Caesar Cipher")
    menu_option = 0
    while menu_option != 1 or menu_option != 2:
        print("Type 1 to encode a message using a key you want. \n")
        print("Type 2 to decode a message using a key you want. \n")
        print("Type 3 to exit. \n")
        menu_option = input()
        if int(menu_option) == 1:
            interface_encode()
        elif int(menu_option) == 2:
            interface_decode()
        elif int(menu_option) == 3:
            break
        else:
            print("Select a correct mode.")


def interface_encode():
    chave = input("Type a number to use as key to encode: ")
    mensagem  = input("Type a message to encode: (ALL CAPS) ")
    mensagem_encoded = cesar_encode(mensagem, int(chave))
    print("Message Encoded: " + mensagem_encoded)

def interface_decode():
    chave = input("Type a number to use as key to decode: ")
    mensagem  = input("Type a message to decode: (ALL CAPS) ")
    message_decoded = cesar_decode(mensagem, int(chave))
    print("Message Decoded: " + message_decoded)


if __name__ == "__main__":
    main()
