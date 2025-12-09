from controller.controller import ControllerCadastro, ControllerLogin, ControllerPerfil
from exceptions.exceptions import *
from os import system
from time import sleep


def menu_principal():  # Menu principal (incompleto)
    pass


def menu_cadastrar():  # Menu de cadastro de usuário
    print("\n===== Cadastrar Usuário =====")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    try:
        ControllerCadastro.cadastrar(nome, email, senha)
        print("\nUsuário cadastrado com sucesso!")
    except NomeInvalidoError as e:
        print(f"\n{e}")
    except EmailInvalidoError as e:
        print(f"\n{e}")
    except SenhaInvalidaError as e:
        print(f"\n{e}")
    except UsuarioJaCadastradoError as e:
        print(f"\n{e}")
    except Exception as e:
        print(f"\nError: {e}")


def menu_login():  # Menu de login de usuário
    try:
        print("\n===== Login de Usuário =====")
        email = input("Email: ")
        senha = input("Senha: ")

        resultado = ControllerLogin.logar(email, senha)

        if resultado:
            print(f"\nLogin realizado com sucesso!")
            sleep(1)
            system('cls')
            sub_menu_login(email)
    except Exception as e:
        print(f"\n{e}")


def sub_menu_login(email):  # Submenu após login bem-sucedido
    while True:
        print("\n===== Menu Perfil =====")
        print("1 - Ver Perfil")
        print("2 - Trocar Senha")
        print("3 - Logout")
        print("=======================\n")
        escolha_perfil = input("Informe uma das opções acima: ")
        system('cls')
        if escolha_perfil == '1':  # Ver Perfil
            usuario = ControllerPerfil.get_perfil(email)
            print(f"\n===== Dados do Usuário =====")
            print(f"ID: {usuario.id}")
            print(f"Nome: {usuario.nome}")
            print(f"Email: {usuario.email}")
            print(f"============================")  # Fim dos dados do usuário
            input("\nPressione ENTER para voltar...")
            system('cls')
        elif escolha_perfil == '2':  # Trocar Senha
            print("\n===== Trocar Senha =====")
            senha_atual = input("Senha Atual: ")
            nova_senha = input("Nova Senha: ")
            try:
                resultado = ControllerPerfil.trocar_senha(
                    email, senha_atual, nova_senha)
                print(resultado)
            except SenhaInvalidaError as e:
                print(f"\n{e}")
            input("\nPressione ENTER para voltar...")
            system('cls')
        elif escolha_perfil == '3':  # Logout
            break
        system('cls')
