class Tarefa:
    def __init__(self, descricao, data):
        self.descricao = descricao
        self.data = data
        self.concluida = False

    def marcarComoConcluida(self):
        self.concluida = True

    def paraDicionario(self):
        return {
            'descricao': self.descricao,
            'data': self.data,
            'concluida': self.concluida
        }

    @staticmethod
    def deDicionario(dados):
        tarefa = Tarefa(dados['descricao'], dados['data'])
        tarefa.concluida = dados['concluida']
        return tarefa
