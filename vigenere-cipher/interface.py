from vigenere import key_gen, encryption, decryption


def menu():
    menu_key = 0
    while menu_key != 3:
        print("\nBem Vindo ao Sistema de Criptografia de Vigenere\n")
        print("Digite 1 para cifrar/decifrar uma mensagem")
        print("Digite 2 para tentar recuperar uma mensagem")
        print("Digite 3 para voltar")
        menu_key = input("\n: ")
        menu_key = int(menu_key)
        if menu_key == 1:
            menu_cipher_mode()
        elif menu_key == 2:
            return
        elif menu_key == 3:
            break
        else:
            print("\nDigite uma opcao valida!")
def menu_cipher_mode():
    menu_key = 0
    while menu_key != 3:
        print("Digite 1 para cifrar uma mensagem\nDigite 2 para decifrar um criptograma\nDigite 3 para sair")
        menu_key = int(input("\n: "))
        if menu_key == 1:
            key_base = input("Digite a chave: ")
            message = input("Digite a mensagem para ser cifrada: ")
            print("Cifrando...")
            key = key_gen(key_base, message)
            print('Messagem: ', message)
            print('Chave gerada: ', key)
            criptogram = encryption(key_base, message)
            print('\nMensagem Cifrada: ', criptogram , "\n")
        elif menu_key == 2:
            key = input("Digite a chave: ")
            criptogram = input("Digite o criptograma: ")
            print("Decifrando...")
            print('Criptograma: ', criptogram)
            print('Chave: ', key)
            message = decryption(key, criptogram)
            print('\nMensagem Decifrada: ', message, "\n")
        elif menu_key == 3:
            break
        else:
            print("Digite uma opcao valida!")
