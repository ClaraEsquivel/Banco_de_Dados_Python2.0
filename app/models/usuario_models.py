from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):

        self.nome = self._verificar_usuario_nome(nome)
        self.email = self._verificar_usuario_email(email)
        self.senha = self._verificar_usuario_senha(senha)


    def _verificar_usuario_nome(self, nome):
        self._verificar_nome_tipo_invalido(nome)
        self._verificar_nome_vazio(nome)

        self.nome = nome
        return self.nome
    

    def _verificar_usuario_email(self, email):
        self._verificar_email_tipo_invalido(email)
        self._verificar_email_vazio(email)

        self.email = email
        return self.email
    

    def _verificar_usuario_senha (self, senha):
        self._verificar_senha_tipo_invalido(senha)
        self._verificar_senha_vazio(senha)

        self.senha = senha
        return self.senha
    

    def _verificar_nome_tipo_invalido(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser um texto")
        return nome
 

    def _verificar_nome_vazio(self, nome):
        if not nome.strip():
            raise ValueError("O nome não deve estar vazio.")
        return nome
    

    def _verificar_email_tipo_invalido(self, email):
        if not isinstance(email, str):
            raise TypeError("O email deve ser um texto")
        return email

    def _verificar_email_vazio(self, email):
        if not email.strip():
            raise ValueError("O email não deve estar vazio.")
        return email


    def _verificar_senha_tipo_invalido(self, senha):
        if not isinstance(senha, str):
            raise TypeError("A senha deve ser um texto")
        return senha
    

    def _verificar_senha_vazio(self, senha):
        if not senha.strip():
            raise ValueError("A senha não deve estar vazia.")
        return senha


# Criando tabela no banco de dados
Base.metadata.create_all(bind=db)

