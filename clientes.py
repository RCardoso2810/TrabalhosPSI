# clientes.py
import random

nomes = ("João", "Maria", "Carlos", "Ana", "Rita", "Pedro", "Sofia", "Miguel")
sexos = ("M", "F")

def gerar_cliente(ronda):
    nome = random.choice(nomes)
    idade = random.randint(18, 70)
    sexo = random.choice(sexos)

    if idade <= 25:
        categoria = "Jovem"
    elif idade <= 50:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    chance_roubo = min(10 + ronda * 3, 50)
    e_ladrao = random.randint(1,100) <= chance_roubo

    # Tuplo do cliente: (nome, idade, sexo, categoria, e_ladrao, banido, chateado, chance_roubo)
    return (nome, idade, sexo, categoria, e_ladrao, False, False, chance_roubo)
