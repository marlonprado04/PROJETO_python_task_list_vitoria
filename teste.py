import json
from datetime import datetime


class Tarefa:
    def __init__(self, titulo, descricao, status="A fazer"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
        self.data_criacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data_conclusao = None
        self.projeto = None
        self.usuario_atribuido = None

    def atualizar_status(self, novo_status):
        self.status = novo_status

    def atualizar_descricao(self, nova_descricao):
        self.descricao = nova_descricao

    def concluir_tarefa(self):
        self.status = "Concluída"
        self.data_conclusao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.tarefas_atribuidas = []

    def criar_tarefa(self, titulo, descricao):
        nova_tarefa = Tarefa(titulo, descricao)
        self.tarefas_atribuidas.append(nova_tarefa)
        return nova_tarefa

    def marcar_tarefa_concluida(self, tarefa):
        tarefa.concluir_tarefa()


class Projeto:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def status_geral(self):
        tarefas_concluidas = sum(
            1 for tarefa in self.tarefas if tarefa.status == "Concluída"
        )
        total_tarefas = len(self.tarefas)
        return f"Conclusão do projeto: {tarefas_concluidas}/{total_tarefas}"


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.projetos = []
        self.carregar_dados()

    def salvar_dados(self):
        dados = {
            "usuarios": [
                {"nome": usuario.nome, "email": usuario.email}
                for usuario in self.usuarios
            ],
            "projetos": [
                {"nome": projeto.nome, "descricao": projeto.descricao}
                for projeto in self.projetos
            ],
            "tarefas": [
                {
                    "titulo": tarefa.titulo,
                    "descricao": tarefa.descricao,
                    "status": tarefa.status,
                    "data_criacao": tarefa.data_criacao,
                    "data_conclusao": tarefa.data_conclusao,
                    "projeto": tarefa.projeto.nome if tarefa.projeto else None,
                    "usuario_atribuido": tarefa.usuario_atribuido.nome
                    if tarefa.usuario_atribuido
                    else None,
                }
                for tarefa in sum([projeto.tarefas for projeto in self.projetos], [])
            ],
        }
        with open("dados.json", "w") as arquivo:
            json.dump(dados, arquivo)

    def carregar_dados(self):
        try:
            with open("dados.json", "r") as arquivo:
                dados = json.load(arquivo)

            for usuario_info in dados["usuarios"]:
                usuario = Usuario(usuario_info["nome"], usuario_info["email"])
                self.usuarios.append(usuario)

            for projeto_info in dados["projetos"]:
                projeto = Projeto(projeto_info["nome"], projeto_info["descricao"])
                self.projetos.append(projeto)

            for tarefa_info in dados["tarefas"]:
                tarefa = Tarefa(
                    tarefa_info["titulo"],
                    tarefa_info["descricao"],
                    tarefa_info["status"],
                )
                tarefa.data_criacao = tarefa_info["data_criacao"]
                tarefa.data_conclusao = tarefa_info["data_conclusao"]
                tarefa.projeto = next(
                    (
                        projeto
                        for projeto in self.projetos
                        if projeto.nome == tarefa_info["projeto"]
                    ),
                    None,
                )
                tarefa.usuario_atribuido = next(
                    (
                        usuario
                        for usuario in self.usuarios
                        if usuario.nome == tarefa_info["usuario_atribuido"]
                    ),
                    None,
                )

                if tarefa.projeto:
                    tarefa.projeto.adicionar_tarefa(tarefa)

                if tarefa.usuario_atribuido:
                    tarefa.usuario_atribuido.tarefas_atribuidas.append(tarefa)

        except FileNotFoundError:
            # Arquivo não existe, pode ser a primeira execução do sistema
            pass

    def encerrar_sistema(self):
        self.salvar_dados()
        exit()

    def exibir_menu_principal(self):
        while True:
            print("### MENU PRINCIPAL ###")
            print("1. Lista de TAREFAS")
            print("2. Lista de PROJETOS")
            print("3. Lista de USUÁRIOS")
            print("4. Encerrar Sistema")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.exibir_lista_tarefas()
            elif escolha == "2":
                self.exibir_lista_projetos()
            elif escolha == "3":
                self.exibir_lista_usuarios()
            elif escolha == "4":
                self.encerrar_sistema()
            else:
                print("Opção inválida. Tente novamente.")

    def exibir_lista_tarefas(self):
        print("\n### LISTA DE TAREFAS ###")
        for projeto in self.projetos:
            for tarefa in projeto.tarefas:
                print(
                    f"Título: {tarefa.titulo}, Descrição: {tarefa.descricao}, "
                    f"Status: {tarefa.status}, Projeto: {projeto.nome}, "
                    f"Usuário Atribuído: {tarefa.usuario_atribuido.nome if tarefa.usuario_atribuido else 'Não atribuído'}"
                )

        while True:
            print("\nOpções:")
            print("1. Selecionar uma tarefa")
            print("2. Voltar ao menu anterior")
            print("3. Encerrar Sistema")

            escolha = input("Escolha uma opção: ")

            if escolha == "1":
                self.selecionar_tarefa()
            elif escolha == "2":
                return
            elif escolha == "3":
                self.encerrar_sistema()
            else:
                print("Opção inválida. Tente novamente.")

    def selecionar_tarefa(self):
        # Lógica para permitir que o usuário selecione e interaja com uma tarefa específica
        pass

    def exibir_lista_projetos(self):
        # Lógica para exibir a lista de projetos e interagir com eles
        pass

    def exibir_lista_usuarios(self):
        # Lógica para exibir a lista de usuários e interagir com eles
        pass


# Exemplo de uso do sistema:

sistema = Sistema()
sistema.exibir_menu_principal()
