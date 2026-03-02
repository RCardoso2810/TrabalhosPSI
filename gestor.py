from aluno import Aluno
from datetime import date, timedelta


class GestorEvento:
    def __init__(self):
        self.alunos = []
        self.turmas = []
        self.eventos = []
        self.evento_atual = None
        self.dia_atual_sistema = date.today()  # Horário atual do sistema
        self.turmas_disponiveis = ["10A", "10B", "10C", "11A", "11B", "11C", "12A", "12B", "12C"]

    def avancar_tempo(self, dias):
        self.dia_atual_sistema += timedelta(days=dias)
        print(f"Tempo avançado! Hoje é: {self.dia_atual_sistema.strftime('%d/%m/%Y')}")

    def criar_evento(self, evento):
        self.eventos.append(evento)
        self.evento_atual = evento
        self.turmas = []
        self.alunos = []
        print("Evento criado e definido como evento atual.")

    def configurar_turmas_evento(self):
        if self.evento_atual is None:
            print("Crie primeiro um evento.")
            return
        print("\nTurmas disponíveis:")
        for i, turma in enumerate(self.turmas_disponiveis):
            print(i, "-", turma)

        indices = input("Escolha os números das turmas (ex: 0 1 3): ").split()
        for idx in indices:
            t = self.turmas_disponiveis[int(idx)]
            if t not in self.turmas:
                self.turmas.append(t)
        print("Turmas configuradas.")

    def adicionar_aluno(self, nome, indice_turma):
        if 0 <= indice_turma < len(self.turmas):
            self.alunos.append(Aluno(nome, self.turmas[indice_turma]))
        else:
            print("Turma inválida.")

    def ver_estatisticas(self):
        if not self.evento_atual:
            print("Sem evento.")
            return

        p = self.evento_atual.preco
        # Regra: Só vai quem marcou 'True' E pagou o total.
        vao = [a for a in self.alunos if a.vai_evento and a.pagou_total(p)]
        # Regra: Quem não pagou ou marcou 'False' vai para os que não vão.
        nao_vao = [a for a in self.alunos if not a.vai_evento or not a.pagou_total(p)]

        print(f"\n--- RELATÓRIO: {self.evento_atual.nome} ---")
        print(f"Data de hoje: {self.dia_atual_sistema.strftime('%d/%m/%Y')}")
        print(f"Turmas no evento: {', '.join(self.turmas)}")

        print("\n✅ ALUNOS QUE VÃO (CONFIRMADOS):")
        for a in vao: print(f" - {a.nome} ({a.turma})")

        print("\n❌ ALUNOS QUE NÃO VÃO (NÃO PAGOU OU DESISTIU):")
        for a in nao_vao: print(f" - {a.nome} ({a.turma})")

        print(f"\nTotal confirmados: {len(vao)}")

    def listar_eventos(self):
        if not self.eventos: print("Sem eventos."); return
        for e in sorted(self.eventos, key=lambda x: (x.data[2], x.data[1], x.data[0])):
            print(e)
