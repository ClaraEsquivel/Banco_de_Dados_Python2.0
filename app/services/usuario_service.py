from app.models.usuario_models import Usuario
from app.repositories.usuario_repository import UsuarioRepository


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



    def pesquisar_usuario_por_email(self):
        try:
            print("\n= Consultando os dados de apenas um usuário =")

            email = input("Digite o email do usuário: ")

            usuario = self.repository.pesquisar_usuario_por_email(email=email)

            if usuario:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
            else:
                    print("Usuário não encontrado")

        except TypeError as erro:
            print(f"Erro ao pesquisar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")        



    def atualizar_usuario(self):
        try:
            print("\n= Atualizando os dados de um usuário =")

            email = input("Informe o email do usuário: ")

            usuario_cadastrado = self.repository.pesquisar_usuario_por_email(email=email)

            if usuario_cadastrado:
                usuario_cadastrado.nome = input("Digite o novo nome: ")
                usuario_cadastrado.email = input("Digite o novo email:")
                usuario_cadastrado.senha = input("Digite a nova senha: ")
               
                print("Usuário atualizado com sucesso!")
            else:
                print("Usuário não encontrado")

        except TypeError as erro:
            print(f"Erro ao atualizar o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")                     


    def excluir_usuario(self):
        try:
            print("\n= Excluindo os dados de um usuário =")

            email = input("Digite o email do usuário que será excluído: ")

            usuario = self.repository.pesquisar_usuario_por_email(email=email)

            if usuario:
                self.repository.excluir_usuario(usuario)
                print(f"Usuário {usuario.nome} excluido com sucesso!")
            else:
                print("Usuário não encontrado")
        
        except TypeError as erro:
            print(f"Erro ao excluir o usuário: {erro}")
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")   


    def listar_usuarios(self):       
        lista_usuarios = self.repository.listar_usuarios()
        print("\n= Listando usuários cadastrados =")
        for usuario in lista_usuarios:
            print(
                f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}"
                )