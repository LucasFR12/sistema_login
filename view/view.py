from view.menus import *
from os import system
from time import sleep

def run():
    while True:

        print("\n===== Menu =====")
        print("1 - Cadastrar")
        print("2 - Logar")
        print("3 - Sair")
        print("================")
        escolha = input("Informe uma das opções acima: ")

        if escolha == '1':
            system('cls')
            menu_cadastrar()
       
        elif escolha == '2':
            system('cls')
            menu_login()
     
        elif escolha == '3':
            system('cls')
            print("=" * 24)
            print("Encerrando o sistema...")
            print("=" * 24)
            sleep(1)
            break
        