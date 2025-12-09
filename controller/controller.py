from model.user import Usuario
from model.dao import Session
from exceptions.exceptions import *
from utils.security import validar_senha, hash_senha, verificar_senha


class ControllerCadastro():

    @classmethod
    def verificar_dados(cls, nome, email):  # Valida os dados de entrada

        if len(nome) > 100 or len(nome) < 3:
            raise NomeInvalidoError("Nome deve ter entre 3 e 100 caracteres.")
        elif len(email) > 100 or len(email) < 12:
            raise EmailInvalidoError(
                "Email deve ter entre 12 e 100 caracteres.")

    @classmethod
    def cadastrar(cls, nome, email, senha):  # Cadastra um novo usuário no sistema

        validar_senha(senha)  # Valida a senha
        cls.verificar_dados(nome, email)
        session = Session()
        usuario = session.query(Usuario).filter(
            Usuario.email == email).first()  # Verifica se o usuário já existe

        if usuario:  # (Usuario ja cadastrado!)
            raise UsuarioJaCadastradoError("Usuário já cadastrado no sistema!")
        senha_hash = hash_senha(senha)
        # Cria o objeto usuário
        user = Usuario(nome=nome, email=email, senha=senha_hash)
        session.add(user)
        session.commit()
        session.close()


class ControllerLogin():  # Responsável pelo login dos usuários

    @classmethod
    def logar(cls, email, senha):  # Realiza o login do usuário
        session = Session()
        usuario = session.query(Usuario).filter(
            Usuario.email == email).first()  # Busca o usuário pelo email

        # autenticação falhou
        if not usuario or not verificar_senha(senha, usuario.senha):
            session.close()
            raise EmailOuSenhaIncorretoError("Email ou senha incorretos.")
        return usuario  # autenticação bem-sucedida


class ControllerPerfil():  # Responsável pelas operações do perfil do usuário

    @classmethod
    def get_perfil(cls, email):  # Exibe os dados do perfil do usuário

        session = Session()
        usuario = session.query(Usuario).filter(Usuario.email == email).first()  # Busca o usuário pelo email
        session.close()
        if usuario:
            return usuario  # Retorna o objeto usuário

    @classmethod
    def trocar_senha(cls, email, senha_atual, nova_senha):  # Troca a senha do usuário

        validar_senha(nova_senha)  # Valida a nova senha

        session = Session()
        usuario = session.query(Usuario).filter(
            Usuario.email == email).first()  # Busca o usuário pelo email
        if not verificar_senha(senha_atual, usuario.senha):  # Senha atual incorreta
            session.close()
            raise SenhaInvalidaError("Senha atual incorreta.")

        usuario.senha = hash_senha(nova_senha)  # Atualiza a senha do usuário
        session.commit()
        session.close()
        return f"\nSenha alterada com sucesso!"
