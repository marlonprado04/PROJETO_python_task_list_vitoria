import json
from datetime import datetime
from Tarefa import Tarefa
from Projeto import Projeto
from Usuario import Usuario


class SistemaGerenciamentoTarefas:
    def __init__(self):
        # Inicializa as listas de usuários, tarefas soltas e projetos
        self.usuarios = []
        self.tarefas_soltas = []
        self.projetos = []

    # Operações CRUD para Usuários

    def criar_usuario(self, nome, email):
        # Cria um novo usuário e o adiciona à lista de usuários
        usuario = Usuario(nome, email)
        self.usuarios.append(usuario)
        return usuario

    def listar_usuarios(self):
        # Lista os usuários disponíveis
        for i, usuario in enumerate(self.usuarios):
            print(f"{i + 1}. {usuario.nome}")

    def editar_usuario(self, usuario, nome, email):
        # Edita as informações de um usuário
        usuario.nome = nome
        usuario.email = email

    def excluir_usuario(self, usuario):
        # Exclui um usuário da lista
        self.usuarios.remove(usuario)

    # Operações CRUD para Tarefas Soltas

    def criar_tarefa_solta(self, titulo, descricao):
        # Cria uma nova tarefa solta e a adiciona à lista
        tarefa = Tarefa(titulo, descricao)
        self.tarefas_soltas.append(tarefa)
        return tarefa

    def listar_tarefas_soltas(self):
        # Lista as tarefas soltas disponíveis
        for i, tarefa in enumerate(self.tarefas_soltas):
            print(f"{i + 1}. {tarefa.titulo}")

    def editar_tarefa_solta(self, tarefa, titulo, descricao):
        # Edita as informações de uma tarefa solta
        tarefa.titulo = titulo
        tarefa.descricao = descricao

    def excluir_tarefa_solta(self, tarefa):
        # Exclui uma tarefa solta da lista
        self.tarefas_soltas.remove(tarefa)

    # Operações CRUD para Projetos

    def criar_projeto(self, nome, descricao):
        # Cria um novo projeto e o adiciona à lista de projetos
        projeto = Projeto(nome, descricao)
        self.projetos.append(projeto)
        return projeto

    def listar_projetos(self):
        # Lista os projetos disponíveis
        for i, projeto in enumerate(self.projetos):
            print(f"{i + 1}. {projeto.nome}")

    def editar_projeto(self, projeto, nome, descricao):
        # Edita as informações de um projeto
        projeto.nome = nome
        projeto.descricao = descricao

    def excluir_projeto(self, projeto):
        # Exclui um projeto da lista
        self.projetos.remove(projeto)

    # Operações CRUD para Tarefas em Projetos

    def criar_tarefa_em_projeto(self, projeto, titulo, descricao):
        # Cria uma nova tarefa vinculada a um projeto e a adiciona à lista de tarefas do projeto
        tarefa = Tarefa(titulo, descricao)
        projeto.adicionar_tarefa(tarefa)
        return tarefa

    def listar_tarefas_em_projeto(self, projeto):
        # Lista as tarefas vinculadas a um projeto
        projeto.mostrar_tarefas()

    def editar_tarefa_em_projeto(self, tarefa, titulo, descricao):
        # Edita as informações de uma tarefa vinculada a um projeto
        tarefa.titulo = titulo
        tarefa.descricao = descricao

    def excluir_tarefa_em_projeto(self, projeto, tarefa):
        # Exclui uma tarefa vinculada a um projeto
        projeto.remover_tarefa(tarefa)

    # Operações CRUD para Tarefas Soltas

    def criar_tarefa_solta(self, titulo, descricao):
        # Cria uma nova tarefa solta e a adiciona à lista de tarefas soltas
        tarefa = Tarefa(titulo, descricao)
        self.tarefas_soltas.append(tarefa)
        return tarefa

    def listar_tarefas_soltas(self):
        # Lista as tarefas soltas disponíveis
        for i, tarefa in enumerate(self.tarefas_soltas):
            print(f"{i + 1}. {tarefa.titulo}")

    def editar_tarefa_solta(self, tarefa, titulo, descricao):
        # Edita as informações de uma tarefa solta
        tarefa.titulo = titulo
        tarefa.descricao = descricao

    def excluir_tarefa_solta(self, tarefa):
        # Exclui uma tarefa solta da lista
        self.tarefas_soltas.remove(tarefa)

    def menu_principal(self):
        # Menu principal para interação com o sistema
        while True:
            print("\n----- Menu Principal -----")
            print("1. Operações CRUD de Usuários")
            print("2. Operações CRUD de Tarefas Soltas")
            print("3. Operações CRUD de Projetos")
            print("4. Operações CRUD de Tarefas em Projetos")
            print("5. Operações CRUD de Tarefas Soltas")
            print("6. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.menu_usuarios()
            elif opcao == "2":
                self.menu_tarefas_soltas()
            elif opcao == "3":
                self.menu_projetos()
            elif opcao == "4":
                self.menu_tarefas_em_projetos()
            elif opcao == "5":
                self.menu_tarefas_soltas()
            elif opcao == "6":
                self.salvar_dados()
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_usuarios(self):
        # Menu para operações CRUD de usuários
        while True:
            print("\n----- Menu de Usuários -----")
            print("1. Criar Usuário")
            print("2. Listar Usuários")
            print("3. Editar Usuário")
            print("4. Excluir Usuário")
            print("5. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Digite o nome do usuário: ")
                email = input("Digite o email do usuário: ")
                self.criar_usuario(nome, email)
            elif opcao == "2":
                self.listar_usuarios()
            elif opcao == "3":
                self.listar_usuarios()
                indice = (
                    int(input("Escolha o número do usuário que deseja editar: ")) - 1
                )
                usuario = self.usuarios[indice]
                nome = input("Digite o novo nome do usuário: ")
                email = input("Digite o novo email do usuário: ")
                self.editar_usuario(usuario, nome, email)
            elif opcao == "4":
                self.listar_usuarios()
                indice = (
                    int(input("Escolha o número do usuário que deseja excluir: ")) - 1
                )
                usuario = self.usuarios[indice]
                self.excluir_usuario(usuario)
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_tarefas_soltas(self):
        # Menu para operações CRUD de tarefas soltas
        while True:
            print("\n----- Menu de Tarefas Soltas -----")
            print("1. Criar Tarefa Solta")
            print("2. Listar Tarefas Soltas")
            print("3. Editar Tarefa Solta")
            print("4. Excluir Tarefa Solta")
            print("5. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                titulo = input("Digite o título da tarefa: ")
                descricao = input("Digite a descrição da tarefa: ")
                self.criar_tarefa_solta(titulo, descricao)
            elif opcao == "2":
                self.listar_tarefas_soltas()
            elif opcao == "3":
                self.listar_tarefas_soltas()
                indice = (
                    int(input("Escolha o número da tarefa que deseja editar: ")) - 1
                )
                tarefa = self.tarefas_soltas[indice]
                titulo = input("Digite o novo título da tarefa: ")
                descricao = input("Digite a nova descrição da tarefa: ")
                self.editar_tarefa_solta(tarefa, titulo, descricao)
            elif opcao == "4":
                self.listar_tarefas_soltas()
                indice = (
                    int(input("Escolha o número da tarefa que deseja excluir: ")) - 1
                )
                tarefa = self.tarefas_soltas[indice]
                self.excluir_tarefa_solta(tarefa)
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_projetos(self):
        # Menu para operações CRUD de projetos
        while True:
            print("\n----- Menu de Projetos -----")
            print("1. Criar Projeto")
            print("2. Listar Projetos")
            print("3. Editar Projeto")
            print("4. Excluir Projeto")
            print("5. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Digite o nome do projeto: ")
                descricao = input("Digite a descrição do projeto: ")
                self.criar_projeto(nome, descricao)
            elif opcao == "2":
                self.listar_projetos()
            elif opcao == "3":
                self.listar_projetos()
                indice = (
                    int(input("Escolha o número do projeto que deseja editar: ")) - 1
                )
                projeto = self.projetos[indice]
                nome = input("Digite o novo nome do projeto: ")
                descricao = input("Digite a nova descrição do projeto: ")
                self.editar_projeto(projeto, nome, descricao)
            elif opcao == "4":
                self.listar_projetos()
                indice = (
                    int(input("Escolha o número do projeto que deseja excluir: ")) - 1
                )
                projeto = self.projetos[indice]
                self.excluir_projeto(projeto)
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def menu_tarefas_em_projetos(self):
        # Menu para operações CRUD de tarefas em projetos
        while True:
            print("\n----- Menu de Tarefas em Projetos -----")
            print("1. Criar Tarefa em Projeto")
            print("2. Listar Tarefas em Projeto")
            print("3. Editar Tarefa em Projeto")
            print("4. Excluir Tarefa em Projeto")
            print("5. Voltar")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.listar_projetos()
                indice_projeto = int(input("Escolha o número do projeto: ")) - 1
                projeto = self.projetos[indice_projeto]
                titulo = input("Digite o título da tarefa: ")
                descricao = input("Digite a descrição da tarefa: ")
                self.criar_tarefa_em_projeto(projeto, titulo, descricao)
            elif opcao == "2":
                self.listar_projetos()
                indice_projeto = int(input("Escolha o número do projeto: ")) - 1
                projeto = self.projetos[indice_projeto]
                self.listar_tarefas_em_projeto(projeto)
            elif opcao == "3":
                self.listar_projetos()
                indice_projeto = int(input("Escolha o número do projeto: ")) - 1
                projeto = self.projetos[indice_projeto]
                self.listar_tarefas_em_projeto(projeto)
                indice_tarefa = (
                    int(input("Escolha o número da tarefa que deseja editar: ")) - 1
                )
                tarefa = projeto.lista_de_tarefas[indice_tarefa]
                titulo = input("Digite o novo título da tarefa: ")
                descricao = input("Digite a nova descrição da tarefa: ")
                self.editar_tarefa_em_projeto(tarefa, titulo, descricao)
            elif opcao == "4":
                self.listar_projetos()
                indice_projeto = int(input("Escolha o número do projeto: ")) - 1
                projeto = self.projetos[indice_projeto]
                self.listar_tarefas_em_projeto(projeto)
                indice_tarefa = (
                    int(input("Escolha o número da tarefa que deseja excluir: ")) - 1
                )
                tarefa = projeto.lista_de_tarefas[indice_tarefa]
                self.excluir_tarefa_em_projeto(projeto, tarefa)
            elif opcao == "5":
                break
            else:
                print("Opção inválida. Tente novamente.")

    def salvar_dados(self):
        # Salva os dados em um arquivo JSON
        dados = {
            "usuarios": [vars(usuario) for usuario in self.usuarios],
            "tarefas_soltas": [vars(tarefa) for tarefa in self.tarefas_soltas],
            "projetos": [vars(projeto) for projeto in self.projetos],
        }

        with open("dados.json", "w") as arquivo_json:
            json.dump(dados, arquivo_json)

    def carregar_dados(self):
        # Carrega dados previamente salvos, se disponíveis
        try:
            with open("dados.json", "r") as arquivo_json:
                dados = json.load(arquivo_json)

                for usuario_data in dados["usuarios"]:
                    usuario = Usuario("", "")
                    usuario.__dict__.update(usuario_data)
                    self.usuarios.append(usuario)

                for tarefa_data in dados["tarefas_soltas"]:
                    tarefa = Tarefa("", "")
                    tarefa.__dict__.update(tarefa_data)
                    self.tarefas_soltas.append(tarefa)

                for projeto_data in dados["projetos"]:
                    projeto = Projeto("", "")
                    projeto.__dict__.update(projeto_data)
                    self.projetos.append(projeto)

                print("Dados carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo de dados não encontrado. Inicializando com listas vazias.")


# Adicione a parte abaixo no código para chamar o menu principal

if __name__ == "__main__":
    sistema = SistemaGerenciamentoTarefas()
    sistema.carregar_dados()
    sistema.menu_principal()
