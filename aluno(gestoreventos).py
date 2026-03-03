class Aluno:
    def __init__(self, nome, turma):
        self.nome = nome.strip().upper()
        self.turma = turma
        self.vai_evento = True
        self.pagamentos = 0.0

    def marcar_presenca(self, vai):
        self.vai_evento = vai

    def adicionar_pagamento(self, valor):
        self.pagamentos += valor

    def pagou_total(self, preco_evento):
        return self.pagamentos >= preco_evento

    def __str__(self):
        status = "Vai" if self.vai_evento else "Não vai"
        return f"{self.nome} ({self.turma}) - {status} - Pago: {self.pagamentos}€"
