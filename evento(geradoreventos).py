class Evento:
    def __init__(self, nome, data_texto, data_limite, preco):
        self.nome = nome.strip().upper() # Força Maiúsculas
        self.data = data_texto # Tuplo (d, m, a)
        self.data_limite = data_limite # Tuplo (d, m, a)
        self.preco = preco

    def __str__(self):
        dia, mes, ano = self.data
        return f"\033[94mEvento {self.nome}\033[0m - {dia}|{mes}|{ano}"
