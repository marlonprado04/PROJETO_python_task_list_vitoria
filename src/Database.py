import json

class Database:
    def __init__(self, nome_arquivo="banco_de_dados.json"):
        self.nome_arquivo = nome_arquivo
        # Carrega dados ao iniciar a classe
        self.dados = self._carregar_dados()

    # Carrega dados do arquivo json
    def _carregar_dados(self):
        try:
            # Abre o arquivo no modo de leitura
            with open(self.nome_arquivo, "r") as arquivo:
                # Carrega e retorna os dados do arquivo JSON
                return json.load(arquivo)
        except FileNotFoundError:
            # Se o arquivo não existe, retorna um banco de dados vazio
            return {"usuarios": [], "projetos": [], "tarefas": []}

    # Salva dados no arquivo json
    def _salvar_dados(self):
        # Abre arquivo no modo de escrita
        with open(self.nome_arquivo, "w") as arquivo:
            # Serializa e escreve os dados no arquivo JSON com indentação de 2 espaços
            json.dump(self.dados, arquivo, indent=2)

    # Adiciona usuário e salva no arquivo json
    def adicionar_usuario(self, usuario):
        self.dados["usuarios"].append(usuario)
        self._salvar_dados()

    # Adiciona projeto e salva no arquivo json
    def adicionar_projeto(self, projeto):
        self.dados["projetos"].append(projeto)
        self._salvar_dados()

    # Adiciona tarefa e salva no arquivo json
    def adicionar_tarefa(self, tarefa):
        self.dados["tarefas"].append(tarefa)
        self._salvar_dados()

    # Obtém lista de usuários
    def obter_usuarios(self):
        return self.dados["usuarios"]

    # Obtém lista de projetos
    def obter_projetos(self):
        return self.dados["projetos"]
    
    # Obtém lista de tarefas
    def obter_tarefas(self):
        return self.dados["tarefas"]
