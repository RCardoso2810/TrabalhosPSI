class Evento:
    def __init__(self, nome, data_texto, hora_inicio, hora_fim, preco):
        self.nome = nome
        self.data = data_texto # Formato (dia, mes, ano)
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.preco = preco

    def __str__(self):
        dia, mes, ano = self.data
        return f"Evento {self.nome} - {dia}|{mes}|{ano}"
