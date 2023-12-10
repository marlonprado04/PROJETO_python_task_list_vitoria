import json


class Database:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo
        # Carrega dados ao iniciar a classe
        self.dados = self._carregar_dados()

    # Carrega dados do arquivo jsos
    def _carregar_dados(self):
        try:
            # Abre o arquivo no modo de leitura
            with open(self.nome_arquivo, "r") as arquivo:
                # Lê o conteúdo do arquivo
                conteudo = arquivo.read()
                # Verifica se o arquivo não está vazio
                if conteudo:
                    # Carrega e retorna os dados do arquivo JSON
                    return json.loads(conteudo)
                else:
                    # Se o arquivo está vazio, retorna um banco de dados vazio
                    return {"usuarios": [], "projetos": [], "tarefas": []}
        except FileNotFoundError:
            # Se o arquivo não existe, cria o arquivo e retorna um banco de dados vazio
            self._criar_arquivo()
            return {"usuarios": [], "projetos": [], "tarefas": []}
        except json.decoder.JSONDecodeError:
            # Se o arquivo não contém um JSON válido, retorna um banco de dados vazio
            return {"usuarios": [], "projetos": [], "tarefas": []}

    # Cria o arquivo
    def _criar_arquivo(self):
        with open(self.nome_arquivo, "w") as arquivo:
            # Escreve um JSON vazio no arquivo
            json.dump({"usuarios": [], "projetos": [], "tarefas": []}, arquivo)

    # Salva dados no arquivo json
    def _salvar_dados(self):
        # Abre arquivo no modo de escrita
        with open(self.nome_arquivo, "w") as arquivo:
            # Serializa e escreve os dados no arquivo JSON com indentação de 2 espaços
            json.dump(self._serializar_dados(), arquivo, indent=2)

    # Adiciona usuário e salva no arquivo json
    def adicionar_usuario(self, usuario):
        novo_usuario = usuario.to_dict()
        self.dados["usuarios"].append(novo_usuario)
        self._salvar_dados()

    # Adiciona projeto e salva no arquivo json
    def adicionar_projeto(self, projeto):
        novo_projeto = projeto.to_dict()
        self.dados["projetos"].append(novo_projeto)
        self._salvar_dados()

    # Adiciona tarefa e salva no arquivo json
    def adicionar_tarefa(self, tarefa):
        nova_tarefa = tarefa.to_dict()
        self.dados["tarefas"].append(nova_tarefa)
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

    # Serializa os dados
    def _serializar_dados(self):
        return {
            "tarefas": [tarefa.to_dict() for tarefa in self.dados["tarefas"]],
        }
