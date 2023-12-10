import json
class Database:
    # Inicia a classe informando o nome do arquivo
    def __init__(self, caminho_do_arquivo):
        self.caminho_do_arquivo = caminho_do_arquivo
        self.dados = self.carregar_json()

    # Carrega dados do arquivo de acordo com o caminho passado
    def carregar_json(self):
        try:
            # Abre o arquivo json a partir do caminho informado na construção do objeto
            with open(self.caminho_do_arquivo, 'r') as arquivo:
                # Armazena leitura dos dados em uma variável
                dados = json.load(arquivo)
            # Retorna variável com os dados lidos
            return dados
        except FileNotFoundError:
            # Se não encontrado, o arquivo é criado em branco
            return {'usuarios': [], 'projetos': [], 'tarefas': []}

    # Atualiza o arquivo 
    def atualizar_json(self):
        # Abre o arquivo passado e atualiza os dados
        with open(self.caminho_do_arquivo, 'w') as file:
            #  Adiciona os dados dentro do arquivo
            json.dump(self.dados, file, indent=4)

    # Adiciona informações do usuário ao arquivo
    def adicionar_usuario(self, usuario):
        self.dados['usuarios'].append(usuario.to_dict())
        self.atualizar_json()

    # Adiciona informações do projeto ao arquivo
    def adicionar_projeto(self, projeto):
        self.dados['projetos'].append(projeto.to_dict())
        self.atualizar_json()

    # Adiciona informações da tarefa ao arquivo
    def adicionar_tarefa(self, tarefa):
        self.dados['tarefas'].append(tarefa.to_dict())
        self.atualizar_json()


