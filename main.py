import json
from tarefa import Tarefa


class GerenciadorDeTarefas:
    def __init__(self, arquivo='tarefas.json'):
        self.arquivo = arquivo
        self.listaDeTarefas = self.carregarTarefas()

    def carregarTarefas(self):
        try:
            with open(self.arquivo, 'r') as f:
                dados = json.load(f)
                return [Tarefa.deDicionario(item) for item in dados]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvarTarefas(self):
        try:
            with open(self.arquivo, 'w') as f:
                json.dump([t.paraDicionario() for t in self.listaDeTarefas], f, indent=4)
        except Exception as erro:
            print(f"💥 Ih rapaz, deu ruim ao salvar: {erro}")

    def adicionarTarefa(self):
        descricao = input("O que tu quer fazer? 📝 ")
        data = input("Pra quando é isso aí? (ex: 2025-05-02) 📆 ")
        novaTarefa = Tarefa(descricao, data)
        self.listaDeTarefas.append(novaTarefa)
        self.salvarTarefas()
        print("✅ Pronto! Mais uma missão na lista!")

    def listarTarefas(self):
        if not self.listaDeTarefas:
            print("😴 Tá tranquilo... nenhuma tarefa por aqui.")
            return

        print("📋 Tarefas:")
        for i, tarefa in enumerate(self.listaDeTarefas, 1):
            status = "✔️ Feita" if tarefa.concluida else "❌ Na espera"
            print(f"{i}. [{status}] {tarefa.descricao} - {tarefa.data}")

    def concluirTarefa(self):
        self.listarTarefas()
        try:
            indice = int(input("Qual tarefa você venceu? (número) 🏁 ")) - 1
            if 0 <= indice < len(self.listaDeTarefas):
                self.listaDeTarefas[indice].marcarComoConcluida()
                self.salvarTarefas()
                print("🏆 Vitória! Essa tarefa já era!")
            else:
                print("🤔 Hmm... essa tarefa aí não existe, jovem.")
        except ValueError:
            print("😵 Isso não é um número não, hein.")


def menu():
    gerenciador = GerenciadorDeTarefas()

    while True:
        print("\n🌟 MENU NINJA DAS TAREFAS 🌟")
        print("1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Concluir tarefa")
        print("4 - Sair do dojo 🥋")

        escolha = input("Escolha tua jornada: ")

        if escolha == '1':
            gerenciador.adicionarTarefa()
        elif escolha == '2':
            gerenciador.listarTarefas()
        elif escolha == '3':
            gerenciador.concluirTarefa()
        elif escolha == '4':
            print("👋 Até mais! Vá e vença suas batalhas diárias!")
            break
        else:
            print("😐 Opção inválida... tenta de novo aí, guerreiro.")


if __name__ == '__main__':
    menu()
