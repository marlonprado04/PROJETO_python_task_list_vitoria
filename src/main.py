# Importando as classes
from classes.Tarefa import Tarefa
from classes.Projeto import Projeto
from classes.Usuario import Usuario

import Menus

# Loop principal do programa
while True:
    Menus.exibir_menu_principal()

    # Solicita a escolha do usuário
    escolha = input("\nEscolha uma opção (1-6): ")

    # Verifica a escolha do usuário
    if escolha == "1":
        Menus.exibir_menu_tarefa()

    elif escolha == "2":
        Menus.exibir_menu_projeto()

    elif escolha == "3":
        Menus.exibir_menu_usuario()
    else:
        print("\nOpção inválida. Por favor, escolha uma opção válida.\n")
