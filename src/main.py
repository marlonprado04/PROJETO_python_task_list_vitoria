import json

from classes.Tarefa import Tarefa
from classes.Projeto import Projeto
from classes.Usuario import Usuario


def salvar_dados(usuarios):
    with open("dados.json", "w") as file:
        json.dump(usuarios, file, default=lambda o: o.__dict__, indent=2)


def carregar_dados():
    try:
        with open("dados.json", "r") as file:
            dados = json.load(file)
            return dados
    except FileNotFoundError:
        return []


usuarios = carregar_dados()

while True:
    print("\n=== MENU ===")
    print("1. Criar Usuário")
    print("2. Listar Usuários")
    print("3. Criar Projeto")
    print("4. Listar Projetos de um Usuário")
    print("5. Criar Tarefa")
    print("6. Listar Tarefas de um Projeto")
    print("0. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Digite o nome do usuário: ")
        email = input("Digite o email do usuário: ")
        usuario = Usuario(nome, email)
        usuarios.append(usuario)
        print("Usuário criado com sucesso!")

    elif escolha == "2":
        for i, user in enumerate(usuarios, start=1):
            print(f"{i}. {user}")

    elif escolha == "3":
        nome_projeto = input("Digite o nome do projeto: ")
        descricao_projeto = input("Digite a descrição do projeto: ")
        projeto = Projeto(nome_projeto, descricao_projeto)

        print("Usuários disponíveis:")
        for i, user in enumerate(usuarios, start=1):
            print(f"{i}. {user}")

        escolha_usuario = (
            int(input("Escolha o número do usuário para associar ao projeto: ")) - 1
        )
        if 0 <= escolha_usuario < len(usuarios):
            usuarios[escolha_usuario].adicionar_projeto(projeto)
            print("Projeto criado e associado ao usuário com sucesso!")
        else:
            print("Escolha de usuário inválida.")

    elif escolha == "4":
        print("Usuários disponíveis:")
        for i, user in enumerate(usuarios, start=1):
            print(f"{i}. {user}")

        escolha_usuario = (
            int(input("Escolha o número do usuário para listar os projetos: ")) - 1
        )
        if 0 <= escolha_usuario < len(usuarios):
            for projeto in usuarios[escolha_usuario].projetos:
                print(projeto)
        else:
            print("Escolha de usuário inválida.")

    elif escolha == "5":
        titulo_tarefa = input("Digite o título da tarefa: ")
        descricao_tarefa = input("Digite a descrição da tarefa: ")
        tarefa = Tarefa(titulo_tarefa, descricao_tarefa)

        print("Projetos disponíveis:")
        for i, user in enumerate(usuarios, start=1):
            print(f"{i}. {user}")

        escolha_usuario = (
            int(
                input(
                    "Escolha o número do usuário para associar a tarefa a um projeto: "
                )
            )
            - 1
        )
        if 0 <= escolha_usuario < len(usuarios):
            usuario = usuarios[escolha_usuario]
            print("Projetos associados ao usuário:")
            for i, projeto in enumerate(usuario.projetos, start=1):
                print(f"{i}. {projeto}")

            escolha_projeto = (
                int(input("Escolha o número do projeto para associar a tarefa: ")) - 1
            )
            if 0 <= escolha_projeto < len(usuario.projetos):
                projeto = usuario.projetos[escolha_projeto]
                projeto.adicionar_tarefa(tarefa)
                print("Tarefa criada e associada ao projeto com sucesso!")
            else:
                print("Escolha de projeto inválida.")
        else:
            print("Escolha de usuário inválida.")

    elif escolha == "6":
        print("Usuários disponíveis:")
        for i, user in enumerate(usuarios, start=1):
            print(f"{i}. {user}")

        escolha_usuario = (
            int(
                input(
                    "Escolha o número do usuário para listar as tarefas de um projeto: "
                )
            )
            - 1
        )
        if 0 <= escolha_usuario < len(usuarios):
            usuario = usuarios[escolha_usuario]
            print("Projetos associados ao usuário:")
            for i, projeto in enumerate(usuario.projetos, start=1):
                print(f"{i}. {projeto}")

            escolha_projeto = (
                int(input("Escolha o número do projeto para listar as tarefas: ")) - 1
            )
            if 0 <= escolha_projeto < len(usuario.projetos):
                projeto = usuario.projetos[escolha_projeto]
                for tarefa in projeto.tarefas:
                    print(tarefa)
            else:
                print("Escolha de projeto inválida.")
        else:
            print("Escolha de usuário inválida.")

    elif escolha == "0":
        salvar_dados(usuarios)
        print("Saindo do programa. Dados salvos em 'dados.json'.")
        break

    else:
        print("Opção inválida. Tente novamente.")
