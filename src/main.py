from classes.Tarefa import Tarefa
from classes.Projeto import Projeto
from classes.Usuario import Usuario
from classes.Database import Database

# Criando instância dos dados
db = Database("./data/dados.json")


# Adiciona dados de exemplo em Tarefas e Projetos para testes


# Pula o número informado de linhas
def pula_linhas(numero_de_linhas):
    print('\n' * numero_de_linhas)

# Apresenta o menu de tarefas
def menu_tarefas():
    while True:
        # Exibe o menu de opções
        pula_linhas(1)
        
        print("---------------------------")
        print("----- MENU DE TAREFAS -----")
        print("---------------------------")
        print("1. Listar tarefa")
        print("2. Adicionar tarefa")
        print("3. Atualizar informações da tarefa")
        print("4. Atualizar status da tarefa")
        print("5. Remover tarefa")
        print("v. Voltar ao menu principal")
        print("e. Encerrar programa")
        
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
                
            pass
        elif opcao_tarefa == '2':
            # Recebe informações para armazenar na nova tarefa 
            pula_linhas(1)
            titulo = input("Digite o título: ")
            descricao = input("Digite a descrição: ")
            pula_linhas(1)
            
            # Cria uma nova tarefa e atualiza sua descrição em seguida
            tarefa = Tarefa(titulo)
            tarefa.atualizar_descricao(descricao)
            
            # Adiciona tarefa criada no arquivo json e printa o resultado da execução
            print(db.adicionar_tarefa(tarefa))
                        
            pass
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
            
            # Armazena informações atualizadas
            titulo = input("Digite o novo título: ") 
            descricao = input("Digite a nova descrição: ")
            
            # Cria uma instância com os valores extraídos do JSON
            tarefa = Tarefa.criar_tarefa_a_partir_de_dict(tarefa_no_banco)
            
            # Armazena os novos valores na tarefa instanciada
            tarefa.atualizar_descricao(descricao)
            tarefa.atualizar_titulo(titulo)
            
            # Armazena a informação atualizada no JSON e printa mensagem
            pula_linhas(1)
            print(db.atualizar_tarefa(numero, tarefa)) 
            pass
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
            
            pass
        elif opcao_tarefa == '5':
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
            pass
        elif opcao_tarefa == 'v':
            break
        elif opcao_tarefa == 'e':
            exit()
        else:
            print("Opção inválida. Tente novamente.")

# Apresenta o menu de projeto
def menu_projeto():
    while True:
        # Exibe o menu de opções
        pula_linhas(1)
        
        print("----------------------------")
        print("----- MENU DE PROJETOS -----")
        print("----------------------------")
        print("1. Listar projetos")
        print("2. Adicionar projeto")
        print("3. Atualizar informações de um projeto")
        print("4. Adicionar tarefa a um projeto")
        print("5. Remover tarefa de um projeto")
        print("6. Listar tarefas de um projeto")
        print("7. Remover projeto")
        print("v. Voltar ao menu principal")
        print("e. Encerrar programa")
        
        pula_linhas(1)
        
        # Armazena opção digitada pelo usuário
        opcao_projeto = input("Digite a opção desejada para projetos: ")
        
        pula_linhas(1)

        if opcao_projeto == '1': 
            # Armazena resultado da listagem de projetos em uma variável 
            lista_de_projetos = db.listar_projetos()     
            
            # Imprime na tela as informações de cada projeto na lista
            for projeto in lista_de_projetos:
                print(Projeto.to_line(projeto))
            pass
        elif opcao_projeto == '2':
            # Recebe informações para armazenar no novo projeto 
            pula_linhas(1)
            titulo = input("Digite o título: ")
            descricao = input("Digite a descrição: ")
            pula_linhas(1)
            
            # Cria um novo projeto e atualiza sua descrição em seguida
            projeto = Projeto(titulo)
            projeto.atualizar_descricao(descricao)
            
            # Adiciona projeto criado no arquivo json e printa o resultado da execução
            print(db.adicionar_projeto(projeto))
            pass
        elif opcao_projeto == '3':
            # Armazena resultado da listagem de projetos em uma variável 
            lista_de_projetos = db.listar_projetos()     
            
            # Imprime na tela as informações de cada projeto na lista
            for projeto in lista_de_projetos:
                print(Projeto.to_line(projeto))
            
            # Recebe o ID do projeto desejado
            pula_linhas(1)
            numero = input("Digite o ID do projeto: ")
            pula_linhas(1)
            
            # Informa os dados da projeto selecionado
            print("O projeto selecionado foi: ")
            pula_linhas(1)
            projeto_no_banco = db.consultar_projeto_por_id(numero)
            print(Projeto.to_line(projeto_no_banco))
            pula_linhas(1)
            
            # Armazena informações atualizadas
            titulo = input("Digite o novo título: ") 
            descricao = input("Digite a nova descrição: ")
            
            # Cria uma instância com os valores extraídos do JSON
            projeto = Projeto.criar_projeto_a_partir_de_dict(projeto_no_banco)
            
            # Armazena os novos valores no projeto instanciado
            projeto.atualizar_descricao(descricao)
            projeto.atualizar_titulo(titulo)
            
            # Armazena a informação atualizada no JSON e printa mensagem
            pula_linhas(1)
            print(db.atualizar_projeto(numero, projeto)) 
            pass
        elif opcao_projeto == '4':
            # Armazena resultado da listagem de projetos em uma variável 
            lista_de_projetos = db.listar_projetos()     
            
            # Imprime na tela as informações de cada projeto na lista
            for projeto in lista_de_projetos:
                print(Projeto.to_line(projeto))
            
            # Recebe o ID do projeto desejado
            pula_linhas(1)
            id_projeto = input("Digite o ID do projeto: ")
            pula_linhas(1)
            
            # Informa os dados do projeto selecionado
            print("O projeto selecionado foi: ")
            pula_linhas(1)
            projeto_no_banco = db.consultar_projeto_por_id(id_projeto)
            print(Projeto.to_line(projeto_no_banco))
            pula_linhas(1)
            
            # Imprime mensagem de listas de tarefas
            pula_linhas(1)
            print("Lista de tarefas que podem ser adicionadas:")
            pula_linhas(1)

            # Varre a lista de tarefas fora do projeto selecionado
            for tarefa in db.listar_tarefas_fora_do_projeto(id_projeto):
                # Printa todas as tarefas na estrutura de tarefa
                print(Tarefa.to_line(tarefa))
                
            # Recebe o ID da tarefa a ser adicionada
            pula_linhas(1)
            id_tarefa = input("Digite o ID da tarefa: ")
            pula_linhas(1)
            
            # Armazena os dados da tarefa extraídos do banco através do ID
            tarefa_no_banco = db.consultar_tarefa_por_id(id_tarefa)
            # Cria uma instância de tarefas a partir do dicionário
            tarefa = Tarefa.criar_tarefa_a_partir_de_dict(tarefa_no_banco)
            # Adiciona o ID do projeto na tarefa
            tarefa.adicionar_projeto(id_projeto)
            
            # Cria instância do projeto a partir dos dados do banco
            projeto = Projeto.criar_projeto_a_partir_de_dict(projeto_no_banco)
            projeto.adicionar_tarefa(id_tarefa)
            
            # Atualizando informações no banco de dados
            db.atualizar_tarefa(id_tarefa, tarefa)
            db.atualizar_projeto(id_projeto, projeto)
            
            # Imprime mensagem
            print(f'Tarefa: "{tarefa.obter_titulo()}" adicionada ao projeto "{projeto.obter_titulo()}".')
            
            pass
        elif opcao_projeto == '5':
            # Armazena resultado da listagem de projetos em uma variável 
            lista_de_projetos = db.listar_projetos()     
            
            # Imprime na tela as informações de cada projeto na lista
            for projeto in lista_de_projetos:
                print(Projeto.to_line(projeto))
            
            # Recebe o ID do projeto desejado
            pula_linhas(1)
            id_projeto = input("Digite o ID do projeto: ")
            pula_linhas(1)
            
            # Informa os dados do projeto selecionado
            print("O projeto selecionado foi: ")
            pula_linhas(1)
            projeto_no_banco = db.consultar_projeto_por_id(id_projeto)
            print(Projeto.to_line(projeto_no_banco))
            pula_linhas(1)
            
            # Imprime mensagem de listas de tarefas
            pula_linhas(1)
            print("Lista de tarefas que podem ser removidas:")
            pula_linhas(1)

            # Armazena a lista de tarefas dentro do projeto
            lista_de_tarefas = db.listar_tarefas_dentro_do_projeto(id_projeto)
            
            # Varre a lista de tarefas fora do projeto selecionado
            for tarefa in lista_de_tarefas:
                # Printa todas as tarefas na estrutura de tarefa
                print(Tarefa.to_line(tarefa))
                
            # Recebe o ID da tarefa a ser removida
            pula_linhas(1)
            id_tarefa = input("Digite o ID da tarefa a ser removida: ")
            pula_linhas(1)
            
            # Armazena os dados da tarefa extraídos do banco através do ID
            tarefa_no_banco = db.consultar_tarefa_por_id(id_tarefa)
            # Cria uma instância de tarefas a partir do dicionário
            tarefa = Tarefa.criar_tarefa_a_partir_de_dict(tarefa_no_banco)
            # Adiciona o ID do projeto na tarefa
            tarefa.remover_projeto(id_projeto)
            
            # Cria instância do projeto a partir dos dados do banco
            projeto = Projeto.criar_projeto_a_partir_de_dict(projeto_no_banco)
            projeto.remover_tarefa(id_tarefa)
            
            # Atualiza valores no banco de dados
            db.atualizar_projeto(id_projeto, projeto)
            db.atualizar_tarefa(id_tarefa, tarefa)
            
            # Imprime mensagem
            print(f'Tarefa: "{tarefa.obter_titulo()}" removida do projeto "{projeto.obter_titulo()}".')
            pass
        elif opcao_projeto == '6':
            # Armazena resultado da listagem de projetos em uma variável 
            lista_de_projetos = db.listar_projetos()     
            
            # Imprime na tela as informações de cada projeto na lista
            for projeto in lista_de_projetos:
                print(Projeto.to_line(projeto))
            
            # Recebe o ID do projeto desejado
            pula_linhas(1)
            id_projeto = input("Digite o ID do projeto: ")
            pula_linhas(1)
            
            # Informa os dados do projeto selecionado
            print("O projeto selecionado foi: ")
            pula_linhas(1)
            projeto_no_banco = db.consultar_projeto_por_id(id_projeto)
            print(Projeto.to_line(projeto_no_banco))
            pula_linhas(1)
            
            # Imprime mensagem
            pula_linhas(1)
            print("Abaixo a lista de tarefas do projeto selecionado:")
            pula_linhas(1)
            
            # Cria lista de tarefas 
            lista_de_tarefas = db.listar_tarefas_dentro_do_projeto(id_projeto)
            
            # Imprime as tarefas da lista
            for tarefa in lista_de_tarefas:
                print(f"{Tarefa.to_line(tarefa)}")
                
            pass
        elif opcao_projeto == '7':
            # Armazena resultado da listagem de projetos em uma variável 
            lista_de_projetos= db.listar_projetos()     
            
            # Imprime na tela as informações de cada projeto na lista
            for projeto in lista_de_projetos:
                print(Projeto.to_line(projeto))
            
            # Recebe o número do projeto desejado
            pula_linhas(1)
            numero = input("Digite o ID do projeto: ")
            pula_linhas(1)
            
            # Informa os dados do projeto selecionado
            print("O projeto selecionada foi: ")
            pula_linhas(1)
            projeto_no_banco = db.consultar_projeto_por_id(numero)
            print(Projeto.to_line(projeto_no_banco))
            pula_linhas(1)
            
            # Exclui projeto selecionado
            db.excluir_projeto(numero)
            pass
        elif opcao_projeto == 'v':
            break
        elif opcao_projeto == 'e':
            exit()
        else:
            print("Opção inválida. Tente novamente.")

# Apresenta o menu de usuario
def menu_usuario():
    while True:
        # Exibe o menu de opções
        pula_linhas(1)
        
        print("----------------------------")
        print("----- MENU DE USUÁRIOS -----")
        print("----------------------------")
        print("1. Listar usuários")
        print("2. Adicionar usuário")
        print("3. Atualizar informações de um usuário")
        print("4. Adicionar tarefa a um usuário")
        print("5. Remover tarefa de um usuário")
        print("6. Listar tarefas de um usuário")
        print("7. Remover usuário")
        print("v. Voltar ao menu principal")
        print("e. Encerrar programa")
        
        pula_linhas(1)
        
        # Armazena opção digitada pelo usuário
        opcao_usuario = input("Digite a opção desejada para usuários: ")
        
        pula_linhas(1)
        
        if opcao_usuario == '1': 
            # Armazena resultado da listagem de usuários em uma variável 
            lista_de_usuarios = db.listar_usuarios()     
            
            # Imprime na tela as informações de cada usuário na lista
            for usuario in lista_de_usuarios:
                print(Usuario.to_line(usuario))
            pass
        elif opcao_usuario == '2':
            # Recebe informações para armazenar no novo usuário 
            pula_linhas(1)
            nome = input("Digite o nome: ")
            email = input("Digite o e-mail: ")
            pula_linhas(1)
            
            # Cria um novo usuário e atualiza seu e-mail em seguida
            usuario = Usuario(nome)
            usuario.atualizar_email(email)
            
            # Adiciona usuário criado no arquivo json e printa o resultado da execução
            print(db.adicionar_usuario(usuario))
            pass
        elif opcao_usuario == '3':
            # Armazena resultado da listagem de usuários em uma variável 
            lista_de_usuarios = db.listar_usuarios()     
            
            # Imprime na tela as informações de cada usuário na lista
            for usuario in lista_de_usuarios:
                print(Usuario.to_line(usuario))
            
            # Recebe o ID do usuário desejado
            pula_linhas(1)
            numero = input("Digite o ID do usuário: ")
            pula_linhas(1)
            
            # Informa os dados do usuário selecionado
            print("O usuário selecionado foi: ")
            pula_linhas(1)
            usuario_no_banco = db.consultar_usuario_por_id(numero)
            print(Usuario.to_line(usuario_no_banco))
            pula_linhas(1)
            
            # Armazena informações atualizadas
            nome = input("Digite o novo nome: ") 
            email = input("Digite o novo e-mail: ")
            
            # Cria uma instância com os valores extraídos do JSON
            usuario = Usuario.criar_usuario_a_partir_de_dict(usuario_no_banco)
            
            # Armazena os novos valores no usuário instanciado
            usuario.atualizar_email(email)
            usuario.atualizar_nome(nome)
            
            # Armazena a informação atualizada no JSON e printa mensagem
            pula_linhas(1)
            print(db.atualizar_usuario(numero, usuario)) 
            pass
        elif opcao_usuario == '4':
            # Armazena resultado da listagem de usuários em uma variável 
            lista_de_usuarios = db.listar_usuarios()     
            
            # Imprime na tela as informações de cada usuário na lista
            for usuario in lista_de_usuarios:
                print(Usuario.to_line(usuario))
            
            # Recebe o ID do usuário desejado
            pula_linhas(1)
            id_usuario = input("Digite o ID do usuário: ")
            pula_linhas(1)
            
            # Informa os dados do usuário selecionado
            print("O usuário selecionado foi: ")
            pula_linhas(1)
            usuario_no_banco = db.consultar_usuario_por_id(id_usuario)
            print(Usuario.to_line(usuario_no_banco))
            pula_linhas(1)
            
            # Imprime mensagem de listas de tarefas
            pula_linhas(1)
            print("Lista de tarefas que podem ser adicionadas:")
            pula_linhas(1)

            # Varre a lista de tarefas fora do usuário selecionado
            for tarefa in db.listar_tarefas_fora_do_usuario(id_usuario):
                # Printa todas as tarefas na estrutura de tarefa
                print(Tarefa.to_line(tarefa))
                
            # Recebe o ID da tarefa a ser adicionada
            pula_linhas(1)
            id_tarefa = input("Digite o ID da tarefa: ")
            pula_linhas(1)
            
            # Armazena os dados da tarefa extraídos do banco através do ID
            tarefa_no_banco = db.consultar_tarefa_por_id(id_tarefa)
            # Cria uma instância de tarefas a partir do dicionário
            tarefa = Tarefa.criar_tarefa_a_partir_de_dict(tarefa_no_banco)
            # Adiciona o ID do usuário na tarefa
            tarefa.adicionar_usuario(id_usuario)
            
            # Cria instância do usuário a partir dos dados do banco
            usuario = Usuario.criar_usuario_a_partir_de_dict(usuario_no_banco)
            usuario.adicionar_tarefa(id_tarefa)
            
            # Atualizando informações no banco de dados
            db.atualizar_tarefa(id_tarefa, tarefa)
            db.atualizar_usuario(id_usuario, usuario)
            
            # Imprime mensagem
            print(f'Tarefa: "{tarefa.obter_titulo()}" adicionada ao usuário "{usuario.obter_nome()}".')
            
            pass
        elif opcao_usuario == '5':
            # Armazena resultado da listagem de usuários em uma variável 
            lista_de_usuarios = db.listar_usuarios()     
            
            # Imprime na tela as informações de cada usuário na lista
            for usuario in lista_de_usuarios:
                print(Usuario.to_line(usuario))
            
            # Recebe o ID do usuário desejado
            pula_linhas(1)
            id_usuario = input("Digite o ID do usuário: ")
            pula_linhas(1)
            
            # Informa os dados do usuário selecionado
            print("O usuário selecionado foi: ")
            pula_linhas(1)
            usuario_no_banco = db.consultar_usuario_por_id(id_usuario)
            print(Usuario.to_line(usuario_no_banco))
            pula_linhas(1)
            
            # Imprime mensagem de listas de tarefas
            pula_linhas(1)
            print("Lista de tarefas que podem ser removidas:")
            pula_linhas(1)

            # Armazena a lista de tarefas dentro do usuário
            lista_de_tarefas = db.listar_tarefas_do_usuario(id_usuario)
            
            # Varre a lista de tarefas fora do usuário selecionado
            for tarefa in lista_de_tarefas:
                # Printa todas as tarefas na estrutura de tarefa
                print(Tarefa.to_line(tarefa))
                
            # Recebe o ID da tarefa a ser removida
            pula_linhas(1)
            id_tarefa = input("Digite o ID da tarefa a ser removida: ")
            pula_linhas(1)
            
            # Armazena os dados da tarefa extraídos do banco através do ID
            tarefa_no_banco = db.consultar_tarefa_por_id(id_tarefa)
            # Cria uma instância de tarefas a partir do dicionário
            tarefa = Tarefa.criar_tarefa_a_partir_de_dict(tarefa_no_banco)
            # Adiciona o ID do usuário na tarefa
            tarefa.remover_usuario(id_usuario)
            
            # Cria instância do usuário a partir dos dados do banco
            usuario = Usuario.criar_usuario_a_partir_de_dict(usuario_no_banco)
            usuario.remover_tarefa(id_tarefa)
            
            # Atualiza valores no banco de dados
            db.atualizar_usuario(id_usuario, usuario)
            db.atualizar_tarefa(id_tarefa, tarefa)
            
            # Imprime mensagem
            print(f'Tarefa: "{tarefa.obter_titulo()}" removida do usuário "{usuario.obter_nome()}".')
            pass
        elif opcao_usuario == '6':
            # Armazena resultado da listagem de usuários em uma variável 
            lista_de_usuarios = db.listar_usuarios()     
            
            # Imprime na tela as informações de cada usuário na lista
            for usuario in lista_de_usuarios:
                print(Usuario.to_line(usuario))
            
            # Recebe o ID do usuário desejado
            pula_linhas(1)
            id_usuario = input("Digite o ID do usuário: ")
            pula_linhas(1)
            
            # Informa os dados do usuário selecionado
            print("O usuário selecionado foi: ")
            pula_linhas(1)
            usuario_no_banco = db.consultar_usuario_por_id(id_usuario)
            print(Usuario.to_line(usuario_no_banco))
            pula_linhas(1)
            
            # Imprime mensagem
            pula_linhas(1)
            print("Abaixo a lista de tarefas do usuário selecionado:")
            pula_linhas(1)
            
            # Cria lista de tarefas 
            lista_de_tarefas = db.listar_tarefas_do_usuario(id_usuario)
            
            # Imprime as tarefas da lista
            for tarefa in lista_de_tarefas:
                print(f"{Tarefa.to_line(tarefa)}")
                
            pass
        elif opcao_usuario == '7':
            # Armazena resultado da listagem de usuários em uma variável 
            lista_de_usuarios = db.listar_usuarios()     
            
            # Imprime na tela as informações de cada usuário na lista
            for usuario in lista_de_usuarios:
                print(Usuario.to_line(usuario))
            
            # Recebe o número do usuário desejado
            pula_linhas(1)
            numero = input("Digite o ID do usuário: ")
            pula_linhas(1)
            
            # Informa os dados do usuário selecionado
            print("O usuário selecionada foi: ")
            pula_linhas(1)
            usuario_no_banco = db.consultar_usuario_por_id(numero)
            print(Usuario.to_line(usuario_no_banco))
            pula_linhas(1)
            
            # Exclui usuário selecionado
            db.excluir_usuario(numero)
            pass
        elif opcao_usuario == 'v':
            break
        elif opcao_usuario == 'e':
            exit()
        else:
            # Lógica para opção inválida
            print("Opção inválida. Digite novamente.")

        
        
        
while True:
    pula_linhas(1)
    print("-----------------------------")
    print("------ MENU PRINCIPAL -------")
    print("-----------------------------")
    print("1. Menu de tarefas")
    print("2. Menu de projetos")
    print("3. Menu de usuários")
    print("e. Encerrar programa")
    pula_linhas(1)
    
    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        menu_tarefas()

    elif opcao == '2':
        menu_projeto()

    elif opcao == '3':
        menu_usuario()

    elif opcao == 'e':
        print("Saindo do programa. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
