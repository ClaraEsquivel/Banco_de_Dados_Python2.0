import pytest

from app.models.usuario_models import Usuario

@pytest.fixture
def usuario_valido():
    usuario = Usuario(nome="Clara", email="clara@gmail.com", senha="123")
    return usuario

def test_usuario_nome_valido(usuario_valido):
    assert usuario_valido.nome == "Clara"

def test_usuario_email_valido(usuario_valido):
    assert usuario_valido.email == "clara@gmail.com"

def test_usuario_senha_valida(usuario_valido):
    assert usuario_valido.senha == "123"


def test_usuario_nome_tipo_invalido_mensagem_erro():
    with pytest.raises(TypeError, match="O nome deve ser um texto"):
        Usuario(123, "clara@gmail.com", "123")

def test_usuario_nome_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="O nome não deve estar vazio."):
        Usuario("", "clara@gmail.com", "123")


def test_usuario_email_tipo_invalido_mensagem_erro():
    with pytest.raises(TypeError, match="O email deve ser um texto"):
        Usuario("Clara", 123, "123")

def test_usuario_email_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="O email não deve estar vazio."):
        Usuario("Clara", "", "123")


def test_usuario_senha_tipo_invalido_mensagem_erro():
    with pytest.raises(TypeError, match="A senha deve ser um texto"):
        Usuario("Clara", "clara@gmail.com", 123)

def test_usuario_senha_vazio_retorna_mensagem_excecao():
    with pytest.raises(ValueError, match="A senha não deve estar vazia."):
        Usuario("Clara", "clara@gmail.com", "")        