from classes.Tarefa import Tarefa
from classes.Projeto import Projeto


# Define função para exibir o menu principal
def exibir_menu_principal():
    print("\n----- MENU PRINCIPAL -----")
    print("1. Entrar em tarefas")
    print("2. Entrar em projetos")
    print("3. Entrar em usuários")
    print("4. Sair\n")


def exibir_menu_tarefa():
    print("\n----- MENU DE TAREFAS -----")
    print("1. Listar tarefas pendentes")
    print("2. Listar tarefas concluídas ")
    print("3. Atualizar status da tarefa")
    print("3. Excluir tarefa")
    print("4. Sair\n")


def exibir_menu_projeto():
    print("\n----- MENU DE PROJETOS -----")


def exibir_menu_usuario():
    print("\n----- MENU DE USUÁRIOS -----")


tarefa1 = Tarefa("Minha tarefa", "é essa aqui")

print(tarefa1.to_dict())

tarefa1.atualizar_status()

print(tarefa1.to_dict())