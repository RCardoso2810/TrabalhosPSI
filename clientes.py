import random  # Biblioteca para gerar valores aleatórios

# Lista de nomes possíveis
nomes = ("João", "Maria", "Carlos", "Ana", "Rita", "Pedro", "Sofia", "Miguel")

# Lista de sexos possíveis
sexos = ("M", "F")

# ================================
# FUNÇÃO PARA GERAR UM CLIENTE
# ================================
def gerar_cliente(ronda):
    nome = random.choice(nomes)
    idade = random.randint(18, 70)
    sexo = random.choice(sexos)

    # Definir categoria por idade
    if idade <= 25:
        categoria = "Jovem"
    elif idade <= 50:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    # Chance de roubo entre 5% e 70%
    chance_roubo = random.randint(5, 70)

    # Define se é ladrão com base na chance
    e_ladrao = random.randint(1,100) <= chance_roubo

    # Estrutura do cliente:
    # (nome, idade, sexo, categoria, é_ladrão, banido, chateado, chance_roubo)
    return (nome, idade, sexo, categoria, e_ladrao, False, False, chance_roubo)
