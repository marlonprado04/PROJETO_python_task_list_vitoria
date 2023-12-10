
# Define função para exibir o menu principal
def exibir_menu_principal():
    print("\n----- MENU PRINCIPAL -----")
    print("1. Entrar em tarefas")
    print("2. Entrar em projetos")
    print("3. Entrar em usuários")
    print("4. Sair\n")
    

def exibir_menu_tarefa():
    print("\n----- MENU DE TAREFAS -----")
    print("1. Entrar em tarefas")
    print("2. Entrar em projetos")
    print("3. Entrar em usuários")
    print("4. Sair\n")

def exibir_menu_projeto():
    print("\n----- MENU DE PROJETOS -----")
    print("1. Entrar em tarefas")
    print("2. Entrar em projetos")
    print("3. Entrar em usuários")
    print("4. Sair\n")

def exibir_menu_usuario():
    print("\n----- MENU DE USUÁRIOS -----")
    print("1. Entrar em tarefas")
    print("2. Entrar em projetos")
    print("3. Entrar em usuários")
    print("4. Sair\n")

# Loop principal do programa
while True:
    exibir_menu_principal()

    # Solicita a escolha do usuário
    escolha = input("\nEscolha uma opção (1-6): ")

    # Verifica a escolha do usuário
    if escolha == "1":
        exibir_menu_tarefa()

    elif escolha == "2":
        exibir_menu_projeto()

    elif escolha == "3":
        exibir_menu_usuario()
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
