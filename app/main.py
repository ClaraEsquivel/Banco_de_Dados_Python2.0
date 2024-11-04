from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from models.usuario_models import Usuario
from config.database import Session
import os
import time

while True:

    def main():
        session = Session()
        repository = UsuarioRepository(session)
        service = UsuarioService(repository)

        print("\n= = = SENAI SOLUTION = = = ")
        print("1 \t Adicionar usuário")
        print("2 \t Pesquisar um usuário")
        print("3 \t Atualizar dados de um usuário")
        print("4 \t Excluir um usuário")
        print("5 \t Exibir todos os usuários cadastrados")
        print("0 \t Sair")

        opcao = int(input("\nDigite a opção desejada: "))

        match (opcao):
            case 1:
                nome = input("Digite seu nome: ")
                email = input("Digite seu email: ")
                senha = input("Digite sua senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)

                time.sleep(3)
                input("Precione 'Enter' para retornar ao menu")

            case 2:
                print("\n= Consultando os dados de apenas um usuário =")
                email = input("Digite o email do usuário: ")

                usuario = session.query(Usuario).filter_by(email=email).first()

                if usuario:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                else:
                    print("Usuário não encontrado")

                time.sleep(3)
                input("Precione 'Enter' para retornar ao menu")

            case 3:
                print("\n= Atualizar dados de todos os usuários =")
                email = input("Digite o email do usuário que será corrigido: ")

                usuario = session.query(Usuario).filter_by(email=email).first()

                if usuario:
                    nome = input("Digite seu nome: ")
                    email = input("Digite seu novo email: ")
                    senha = input("Digite sua nova senha: ")
                    # repository.salvar_usuario(usuario)

                    service.atualizar_usuario(nome=nome, email=email, senha=senha)
                    session.commit()

                else:
                    print("Usuário não encontrado!")

                time.sleep(3)
                input("Precione 'Enter' para retornar ao menu")

            case 4:
                print("\n= Excluindo os dados de um usuário =")
                email = input("Digite o email do usuário que será excluído: ")

                usuario = session.query(Usuario).filter_by(email=email).first()

                if usuario:
                    session.delete(usuario)
                    session.commit()
                    print(f"Usuário {usuario.nome} excluido com sucesso!")
                else:
                    print("Usuário não encontrado")

                time.sleep(3)
                input("Precione 'Enter' para retornar ao menu")

            case 5:
                print("\n= Listando usuários cadastrados =")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(
                        f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}"
                    )

                time.sleep(3)
                input("Precione 'Enter' para retornar ao menu")

            case 0:
                print("= = = Saindo do menu = = =")

            case _:
                input("Opção inválida!")

    if __name__ == "__main__":
        os.system("cls||clear")
        main()
