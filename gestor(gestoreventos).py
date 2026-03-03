from aluno import Aluno
from datetime import date, timedelta


class GestorEvento:
    def __init__(self):
        self.alunos = []
        self.turmas = set()  # Uso de SET
        self.eventos = []
        self.evento_atual = None
        self.dia_atual_sistema = date.today()
        self.turmas_disponiveis = ["10A", "10B", "10C", "11A", "11B", "11C", "12A", "12B", "12C"]

    def avancar_tempo(self, dias):
        self.dia_atual_sistema += timedelta(days=dias)
        print(f"\033[93mHoje é: {self.dia_atual_sistema.strftime('%d/%m/%Y')}\033[0m")

    def criar_evento(self, evento):
        self.eventos.append(evento)
        self.evento_atual = evento
        self.turmas = set()
        self.alunos = []
        print("\033[92mEvento criado com sucesso!\033[0m")

    def configurar_turmas_evento(self):
        if not self.evento_atual: return
        print("\nTurmas (0 para voltar):")
        for i, t in enumerate(self.turmas_disponiveis): print(f"{i}-{t}", end=" ")
        entrada = input("\nEscolha os números: ")
        if entrada == '0': return
        for idx in entrada.split():
            if idx.isdigit() and int(idx) < len(self.turmas_disponiveis):
                self.turmas.add(self.turmas_disponiveis[int(idx)])

    def adicionar_aluno(self, nome, indice_turma):
        lista_t = sorted(list(self.turmas))
        if 0 <= indice_turma < len(lista_t):
            self.alunos.append(Aluno(nome, lista_t[indice_turma]))

    def ver_estatisticas(self):
        if not self.evento_atual: return

        # Datas para comparação
        d_e, m_e, a_e = self.evento_atual.data
        d_l, m_l, a_l = self.evento_atual.data_limite
        data_evento_obj = date(a_e, m_e, d_e)
        data_limite_obj = date(a_l, m_l, d_l)

        hoje = self.dia_atual_sistema
        evento_ja_passou = hoje >= data_evento_obj
        prazo_limite_passou = hoje > data_limite_obj

        # Labels dinâmicos
        txt_vão = "FOI" if evento_ja_passou else "VAI"
        txt_não_vão = "NÃO FOI" if evento_ja_passou else "NÃO VAI"

        vao_pagos = [a for a in self.alunos if a.vai_evento and a.pagou_total(self.evento_atual.preco)]
        vao_faltam = [a for a in self.alunos if a.vai_evento and not a.pagou_total(self.evento_atual.preco)]
        desistentes = [a for a in self.alunos if not a.vai_evento]

        print(f"\n\033[95m--- RELATÓRIO: {self.evento_atual.nome} ---\033[0m")

        print(f"\n\033[92m✅ ALUNOS QUE {txt_vão} (PAGO):\033[0m")
        for a in vao_pagos: print(f" - {a.nome}")

        if prazo_limite_passou:
            print(f"\n\033[91m❌ ALUNOS QUE {txt_não_vão} (NÃO PAGOU A TEMPO):\033[0m")
            for a in vao_faltam: print(f" - {a.nome}")
        else:
            print(f"\n\033[93m⏳ ALUNOS QUE {txt_vão} (FALTA PAGAR):\033[0m")
            for a in vao_faltam: print(f" - {a.nome}")

        print(f"\n\033[31m🚪 {txt_não_vão} (DESISTÊNCIAS):\033[0m")
        for a in desistentes: print(f" - {a.nome}")

    def listar_eventos(self):
        for e in self.eventos: print(e)
