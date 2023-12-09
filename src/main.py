from Projeto import Projeto
from Tarefa import Tarefa
from Usuario import Usuario


def exibir_menu():
    print("\n=== MENU ===")
    print("1. Criar Projeto")
    print("2. Adicionar Tarefa ao Projeto")
    print("3. Atribuir Tarefa ao Usuário")
    print("4. Concluir Tarefa")
    print("5. Mostrar Status Geral do Projeto")
    print("6. Listar Usuários")
    print("7. Listar Projetos")
    print("8. Salvar Projeto em JSON")
    print("9. Carregar Projeto de JSON")
    print("10. Sair")


def listar_usuarios(usuarios):
    print("\n=== LISTA DE USUÁRIOS ===")
    for i, usuario in enumerate(usuarios):
        print(f"{i + 1}. {usuario.nome} ({usuario.email})")


def listar_projetos(projetos):
    print("\n=== LISTA DE PROJETOS ===")
    for i, projeto in enumerate(projetos):
        print(f"{i + 1}. {projeto.nome}")


def main():
    usuarios = []  # Lista para armazenar usuários
    projetos = []  # Lista para armazenar projetos
    projeto_atual = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-10): ")

        if opcao == "1":
            nome_projeto = input("Digite o nome do projeto: ")
            descricao_projeto = input("Digite a descrição do projeto: ")
            projeto_atual = Projeto(nome_projeto, descricao_projeto)
            projetos.append(projeto_atual)
            print(f"Projeto '{nome_projeto}' criado com sucesso!")

        elif opcao == "2":
            if projeto_atual is not None:
                titulo_tarefa = input("Digite o título da tarefa: ")
                descricao_tarefa = input("Digite a descrição da tarefa: ")
                tarefa = Tarefa(titulo_tarefa, descricao_tarefa)
                projeto_atual.adicionar_tarefa(tarefa)
                print(f"Tarefa '{titulo_tarefa}' adicionada ao projeto.")
            else:
                print("Crie um projeto primeiro!")

        elif opcao == "3":
            if projeto_atual is not None:
                if projeto_atual.lista_de_tarefas:
                    projeto_atual.mostrar_status_geral_do_projeto()
                    indice_tarefa = int(
                        input("Digite o índice da tarefa a ser atribuída: ")
                    )
                    if 0 <= indice_tarefa < len(projeto_atual.lista_de_tarefas):
                        listar_usuarios(usuarios)
                        indice_usuario = int(input("Digite o índice do usuário: "))
                        if 0 <= indice_usuario < len(usuarios):
                            usuarios[indice_usuario].adicionar_tarefa(
                                projeto_atual.lista_de_tarefas[indice_tarefa]
                            )
                            print(
                                f"Tarefa atribuída ao usuário '{usuarios[indice_usuario].nome}'."
                            )
                        else:
                            print("Índice de usuário inválido!")
                    else:
                        print("Índice de tarefa inválido!")
                else:
                    print("Adicione tarefas ao projeto primeiro!")

            else:
                print("Crie um projeto primeiro!")

        elif opcao == "4":
            if projeto_atual is not None:
                if projeto_atual.lista_de_tarefas:
                    projeto_atual.mostrar_status_geral_do_projeto()
                    indice_tarefa_concluir = int(
                        input("Digite o índice da tarefa a ser concluída: ")
                    )
                    if (
                        0
                        <= indice_tarefa_concluir
                        < len(projeto_atual.lista_de_tarefas)
                    ):
                        projeto_atual.lista_de_tarefas[
                            indice_tarefa_concluir
                        ].atualizar_status()
                        print("Tarefa concluída com sucesso!")
                    else:
                        print("Índice de tarefa inválido!")
                else:
                    print("Adicione tarefas ao projeto primeiro!")

            else:
                print("Crie um projeto primeiro!")

        elif opcao == "5":
            if projeto_atual is not None:
                projeto_atual.mostrar_status_geral_do_projeto()
            else:
                print("Crie um projeto primeiro!")

        elif opcao == "6":
            listar_usuarios(usuarios)

        elif opcao == "7":
            listar_projetos(projetos)

        elif opcao == "8":
            if projeto_atual is not None:
                nome_arquivo = input(
                    "Digite o nome do arquivo JSON para salvar o projeto: "
                )
                projeto_atual.salvar_em_json(nome_arquivo)
                print(f"Projeto salvo em '{nome_arquivo}'.")
            else:
                print("Crie um projeto primeiro!")

        elif opcao == "9":
            nome_arquivo = input(
                "Digite o nome do arquivo JSON para carregar o projeto: "
            )
            projeto_atual = Projeto("", "")
            projeto_atual.carregar_de_json(nome_arquivo)
            projetos.append(projeto_atual)
            print(f"Projeto carregado de '{nome_arquivo}'.")

        elif opcao == "10":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
