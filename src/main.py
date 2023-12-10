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
projeto1 = Projeto("Projeto 1")

# Adicionando a tarefa ao banco de dados
db.adicionar_projeto(projeto1)

# Criando instância da tarefa a partir dos valores do banco
projeto2 = Projeto.criar_projeto_a_partir_de_dict(db.consultar_projeto_por_id(1))

projeto2.adicionar_tarefa(1)

db.atualizar_projeto(1, projeto2)