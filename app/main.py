import os
import sys
import time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.config.database import Session


def main():
        session = Session()
        repository = UsuarioRepository(session)
        service = UsuarioService(repository)

        while True:
            os.system("cls||clear")
            print("\n= = = SENAI SOLUTION = = = ")
            print("1 \t| Adicionar usuário")
            print("2 \t| Pesquisar um usuário")
            print("3 \t| Atualizar dados de um usuário")
            print("4 \t| Excluir um usuário")
            print("5 \t| Exibir todos os usuários cadastrados")
            print("0 \t| Sair")

            opcao = int(input("\nDigite a opção desejada: "))

            match (opcao):
                case 1:
                    os.system("cls||clear")
                    print("\n = Adicionar usuário =")
                    nome = input("Digite o nome: ")
                    email = input("Digite o email: ")
                    senha = input("Digite a senha: ")

                    service.criar_usuario(nome=nome, email=email, senha=senha)
                    
                    time.sleep(3)
                    input("Precione 'Enter' para retornar ao menu")
                

                case 2:
                    os.system("cls||clear")
                    service.listar_usuarios()
                    service.pesquisar_usuario_por_email()
                    session.commit()
                    time.sleep(3)
                    input("Precione 'Enter' para retornar ao menu")


                case 3:
                    os.system("cls||clear") 
                    service.listar_usuarios()
                    service.atualizar_usuario()
                    session.commit()
                    time.sleep(3)
                    input("Precione 'Enter' para retornar ao menu")


                case 4:
                    os.system("cls||clear") 
                    service.listar_usuarios()
                    service.excluir_usuario()
                    session.commit()
                    input("Precione 'Enter' para retornar ao menu")


                case 5:
                    os.system("cls||clear") 
                    service.listar_usuarios()
                    session.commit
                    time.sleep(3)
                    input("Precione 'Enter' para retornar ao menu")


                case 0:
                    os.system("cls||clear")
                    print("= = = Saindo do menu = = =")
                    break
                

                case _:
                    os.system("cls||clear")
                    input("Opção inválida!")


if __name__ == "__main__":
    os.system("cls||clear")
    main()
