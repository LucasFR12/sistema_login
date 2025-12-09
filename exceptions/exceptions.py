class NomeInvalidoError(Exception):
    """Exceção levantada para nomes inválidos."""
    pass

class EmailInvalidoError(Exception):
    """Exceção levantada para emails inválidos."""
    pass

class SenhaInvalidaError(Exception):
    """Exceção levantada para senhas inválidas."""
    pass

class UsuarioJaCadastradoError(Exception):
    """Exceção levantada quando o usuário já está cadastrado."""
    pass

class EmailOuSenhaIncorretoError(Exception):
    """Exceção levantada para email ou senha incorretos."""
    pass