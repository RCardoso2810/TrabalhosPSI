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

    # Chance de roubo aleatória entre 5% e 70%
    chance_roubo = random.randint(5, 70)
    e_ladrao = random.randint(1,100) <= chance_roubo

    return (nome, idade, sexo, categoria, e_ladrao, False, False, chance_roubo)
