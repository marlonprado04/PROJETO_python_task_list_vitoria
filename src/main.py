from classes.Tarefa import Tarefa
from classes.Projeto import Projeto
from classes.Usuario import Usuario
from classes.Database import Database

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



# Exemplo de uso:

# Criando uma instância da classe Database
db = Database("./dados.json")

# Criando uma instância da classe Tarefa
nova_tarefa = Tarefa("Nova Tarefa")
novo_projeto = Projeto("Novo projeto")
novo_usuario = Usuario("Novo usuario")

nova_tarefa1 = Tarefa("Minha nova tarefitcha")

# Adicionando a tarefa ao banco de dados
db.adicionar_tarefa(nova_tarefa)
db.adicionar_tarefa(nova_tarefa)
db.adicionar_tarefa(nova_tarefa)
db.adicionar_tarefa(nova_tarefa1)

print(db.consultar_tarefa_por_id(4))