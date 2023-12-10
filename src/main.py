from classes.Tarefa import Tarefa
from classes.Projeto import Projeto
from classes.Usuario import Usuario
from classes.Database import Database

# Criando instância dos dados
db = Database("./dados.json")

tarefa = Tarefa("Tarefa criada por último")
db.adicionar_tarefa(tarefa)

# Pula o número informado de linhas
def pula_linhas(numero_de_linhas):
    print('\n' * numero_de_linhas)

# Apresenta o menu de tarefas
def menu_tarefas():
    while True:
        # Exibe o menu de opções
        pula_linhas(1)
        
        print("----- MENU DE TAREFAS -----")
        print("1. Listar tarefas")
        print("2. Atualizar informações de alguma tarefa")
        print("3. Atualizar status de alguma tarefa")
        print("4. Remover tarefa")
        print("5. Voltar ao menu principal")
        print("6. Encerrar programa")
        
        pula_linhas(1)
        
        # Armazena opção digitada pelo usuário
        opcao_tarefa = input("Digite a opção desejada para tarefas: ")
        
        pula_linhas(1)

        if opcao_tarefa == '1':     
            # Armazena resultado da listagem de tarefas em uma variável 
            lista_de_tarefas = db.listar_tarefas()     
            
            # Imprime na tela as informações de cada tarefa na lista
            for tarefa in lista_de_tarefas:
                print(Tarefa.to_line(tarefa))
                
            break
        elif opcao_tarefa == '2':
            # Armazena resultado da listagem de tarefas em uma variável 
            lista_de_tarefas = db.listar_tarefas()     
            
            # Imprime na tela as informações de cada tarefa na lista
            for tarefa in lista_de_tarefas:
                print(Tarefa.to_line(tarefa))
            
            # Recebe o número da tarefa desejada
            pula_linhas(1)
            numero = input("Digite o ID da tarefa: ")
            pula_linhas(1)
            
            # Informa os dados da tarefa selecionada
            print("A tarefa selecionada foi: ")
            pula_linhas(1)
            tarefa_no_banco = db.consultar_tarefa_por_id(numero)
            print(Tarefa.to_line(tarefa_no_banco))
            pula_linhas(1)
            
            # Armazena informações atualizadas
            titulo = input("Digite o novo título: ") 
            descricao = input("Digite a nova descrição: ")
            
            # Cria uma instância com os valores extraídos do JSON
            tarefa = Tarefa.criar_tarefa_a_partir_de_dict(tarefa_no_banco)
            
            # Armazena os novos valores na tarefa instanciada
            tarefa.atualizar_descricao(descricao)
            tarefa.atualizar_titulo(titulo)
            
            # Armazena a informação atualizada no JSON
            db.atualizar_tarefa(numero, tarefa) 
            break
        elif opcao_tarefa == '3':
            # Armazena resultado da listagem de tarefas em uma variável 
            lista_de_tarefas = db.listar_tarefas()     
            
            # Imprime na tela as informações de cada tarefa na lista
            for tarefa in lista_de_tarefas:
                print(Tarefa.to_line(tarefa))
            
            # Recebe o número da tarefa desejada
            pula_linhas(1)
            numero = input("Digite o ID da tarefa: ")
            pula_linhas(1)
            
            # Informa os dados da tarefa selecionada
            print("A tarefa selecionada foi: ")
            pula_linhas(1)
            tarefa_no_banco = db.consultar_tarefa_por_id(numero)
            print(Tarefa.to_line(tarefa_no_banco))
            pula_linhas(1)
                        
            # Cria uma instância com os valores extraídos do JSON
            tarefa = Tarefa.criar_tarefa_a_partir_de_dict(tarefa_no_banco)
            
            # Atualiza o status da tarefa instanciada
            tarefa.atualizar_status()
            
            # Armazena a informação atualizada no JSON
            db.atualizar_tarefa(numero, tarefa) 
            
            # Informa que a tarefa teve o status atualizado
            pula_linhas(1)
            print(f"Tarefa: {tarefa_no_banco['titulo']} teve o status atualizado para {tarefa_no_banco['status']}")
            pula_linhas(1)
            
            break
        elif opcao_tarefa == '4':
            # Armazena resultado da listagem de tarefas em uma variável 
            lista_de_tarefas = db.listar_tarefas()     
            
            # Imprime na tela as informações de cada tarefa na lista
            for tarefa in lista_de_tarefas:
                print(Tarefa.to_line(tarefa))
            
            # Recebe o número da tarefa desejada
            pula_linhas(1)
            numero = input("Digite o ID da tarefa: ")
            pula_linhas(1)
            
            # Informa os dados da tarefa selecionada
            print("A tarefa selecionada foi: ")
            pula_linhas(1)
            tarefa_no_banco = db.consultar_tarefa_por_id(numero)
            print(Tarefa.to_line(tarefa_no_banco))
            pula_linhas(1)
            
            # Exclui tarefa selecionada
            db.excluir_tarefa(numero)
            break
        elif opcao_tarefa == '5':
            break
        elif opcao_tarefa == '6':
            exit()
        else:
            print("Opção inválida. Tente novamente.")


while True:
    pula_linhas(1)
    print("----- MENU PRINCIPAL -----")
    print("1. Menu de tarefas")
    print("2. Menu de projetos")
    print("3. Menu de usuários")
    print("4. Encerrar programa")
    pula_linhas(1)
    
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        menu_tarefas()

    elif opcao == '2':
        while True:
            exibir_menu_projeto()
            # Adicione lógica para o menu de projetos

    elif opcao == '3':
        exibir_menu_usuario()
        # Adicione lógica para o menu de usuários

    elif opcao == '4':
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
