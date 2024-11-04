from models.usuario_models import Usuario
from repositories.usuario_repository import UsuarioRepository


class UsuarioService:
    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")

        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_usuarios()


    def atualizar_usuario(self):
        try:
            print("\n= Atualizando os dados de um usuário =")

            email = input("Informe o email do usuário: ")

            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email=email)

            if usuario_cadastrado:
                usuario_cadastrado.nome = input("Digite seu nome: ")
                usuario_cadastrado.email = input("Digite seu novo email:")
                usuario_cadastrado.senha = input("Digite sua nova senha: ")
                self.repository.atualizar_usuario(usuario_cadastrado)
                print("usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado")

        except TypeError as erro:
            print(f"Erro ao atualizar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")                     