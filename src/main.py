from Projeto import Projeto
from Tarefa import Tarefa
from Usuario import Usuario


def exibir_menu():
    print("\n=== MENU ===")
    print("1. Criar Projeto")
    print("2. Adicionar Tarefa a um Projeto")
    print("3. Atribuir Tarefa a um Usuário")
    print("4. Concluir Tarefa")
    print("5. Mostrar Status Geral do Projeto")
    print("6. Salvar Projeto em JSON")
    print("7. Carregar Projeto de JSON")
    print("8. Sair")


def main():
    projeto_atual = None

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-8): ")

        if opcao == "1":
            nome_projeto = input("Digite o nome do projeto: ")
            descricao_projeto = input("Digite a descrição do projeto: ")
            projeto_atual = Projeto(nome_projeto, descricao_projeto)
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
                        nome_usuario = input("Digite o nome do usuário: ")
                        email_usuario = input("Digite o email do usuário: ")
                        usuario = Usuario(nome_usuario, email_usuario)
                        usuario.adicionar_tarefa(
                            projeto_atual.lista_de_tarefas[indice_tarefa]
                        )
                        print(f"Tarefa atribuída ao usuário '{nome_usuario}'.")
                    else:
                        print("Índice inválido!")
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
                        print("Índice inválido!")
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
            if projeto_atual is not None:
                nome_arquivo = input(
                    "Digite o nome do arquivo JSON para salvar o projeto: "
                )
                projeto_atual.salvar_em_json(nome_arquivo)
                print(f"Projeto salvo em '{nome_arquivo}'.")
            else:
                print("Crie um projeto primeiro!")

        elif opcao == "7":
            nome_arquivo = input(
                "Digite o nome do arquivo JSON para carregar o projeto: "
            )
            projeto_atual = Projeto("", "")
            projeto_atual.carregar_de_json(nome_arquivo)
            print(f"Projeto carregado de '{nome_arquivo}'.")

        elif opcao == "8":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
