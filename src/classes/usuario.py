class Usuario:
	def __init__(self, nome, email):
		self.nome = nome
		self.email = email
		self.tarefas_atribuidas = []

	def criar_tarefa(self, titulo, descricao, status, data_criacao, data_conclusao=None):
		# Implemente conforme necessário
		pass

	def alterar_status_tarefa(self, tarefa, novo_status):
		# Implemente conforme necessário
		pass
