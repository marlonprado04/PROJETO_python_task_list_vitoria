from classes.Tarefa import Tarefa
from classes.Projeto import Projeto
from classes.Usuario import Usuario


def menu():
    print("\n===== MENU =====")
    print("1. Criar Tarefa")
    print("2. Criar Projeto")
    print("3. Listar Projetos Pendentes por Usuário")
    print("4. Sair")


def main():
    usuarios = []  # Armazenará todos os usuários

    while True:
        menu()
        escolha = input("Escolha uma opção (1-4): ")

        if escolha == "1":
            # Criar Tarefa
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            status = input("Digite o status da tarefa: ")
            data_criacao = input("Digite a data de criação da tarefa: ")

            nova_tarefa = Tarefa(
                titulo, descricao, status, data_criacao
            )

            # Adicionar tarefa a um projeto existente ou criar um novo projeto
            projeto_nome = input("Digite o nome do projeto (ou deixe em branco para criar um novo): ")
            if projeto_nome:
                # Adicionar a tarefa a um projeto existente
                projeto_encontrado = False
                for usuario in usuarios:
                    for projeto in usuario.projetos:
                        if projeto.nome == projeto_nome:
                            projeto.adicionar_tarefa(nova_tarefa)
                            projeto_encontrado = True
                            break
                if not projeto_encontrado:
                    print(f"Projeto '{projeto_nome}' não encontrado.")
            else:
                # Criar um novo projeto e adicionar a tarefa
                projeto_nome = input("Digite o nome do novo projeto: ")
                projeto_descricao = input("Digite a descrição do novo projeto: ")
                usuario_atual.criar_projeto(projeto_nome, projeto_descricao).adicionar_tarefa(nova_tarefa)

        elif escolha == "2":
            # Criar Projeto
            nome_projeto = input("Digite o nome do projeto: ")
            descricao_projeto = input("Digite a descrição do projeto: ")
            usuario_atual.criar_projeto(nome_projeto, descricao_projeto)

        elif escolha == "3":
            # Listar Projetos Pendentes por Usuário
            for usuario in usuarios:
                print(f"\nProjetos pendentes para {usuario.nome}:")
                for projeto in usuario.projetos:
                    print(f"\nProjeto: {projeto.nome}")
                    for tarefa in projeto.listar_tarefas():
                        print(f"Tarefa: {tarefa.titulo} - Status: {tarefa.status}")

        elif escolha == "4":
            # Sair do programa
            print("\nSaindo do programa.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    usuario_atual = Usuario("Nome do Usuário", "usuario@email.com")
    usuarios.append(usuario_atual)
    main()
