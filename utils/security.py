from passlib.hash import argon2
from exceptions.exceptions import *

def validar_senha(senha: str): # Valida a senha conforme critérios de segurança
    
    if not isinstance(senha, str): # Verifica se a senha é uma string
        raise SenhaInvalidaError("Senha deve ser uma string.")

    if len(senha) < 6:
        raise SenhaInvalidaError("Senha deve ter no mínimo 6 caracteres.")
    
def hash_senha(senha: str) -> str: # Gera o hash da senha
    return argon2.hash(senha)

def verificar_senha(senha: str, hash_senha: str) -> bool: # Verifica se a senha corresponde ao hash
    return argon2.verify(senha, hash_senha)