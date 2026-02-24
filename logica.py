import random  # Biblioteca para números aleatórios

# ================================
# CORES ANSI PARA O TERMINAL
# ================================
COR_RESET = '\033[0m'
COR_TITULO = '\033[35m'
COR_DESTAQUE = '\033[36m'
COR_SUCESSO = '\033[32m'
COR_ERRO = '\033[31m'
COR_AVISO = '\033[33m'
COR_TEXTO = '\033[37m'

# Imprime uma linha decorativa
def linha():
    print(f"{COR_DESTAQUE}" + "="*50 + f"{COR_RESET}")

# Mostra informações do cliente
def mostrar_cliente(cliente):
    nome, idade, sexo, categoria, e_ladrao, banido, chateado, chance_roubo = cliente
    linha()
    print(f"{COR_TITULO}CLIENTE: {nome}{COR_RESET}")
    print(f"{COR_TEXTO}Idade: {idade} | Sexo: {sexo} | Categoria: {categoria}{COR_RESET}")
    print(f"{COR_AVISO}Chance de roubo: {chance_roubo}%{COR_RESET}")

# ==========================================
# PROCESSA A COMPRA DE UM CLIENTE
# ==========================================
def processar_compra(cliente, produtos, caixa, clientes_banidos):

    # Desempacotar cliente
    nome, idade, sexo, categoria, e_ladrao, banido, chateado, chance_roubo = cliente

    # Variáveis de controlo
    vendidos = 0
    roubos = 0
    dinheiro_recebido = 0
    clientes_insatisfeitos = 0

    # Verificar se cliente está banido
    foi_banido = False
    for b in clientes_banidos:
        if b[0] == nome:
            foi_banido = True
            break

    # Se cliente banido voltar
    if foi_banido:
        print(f"{COR_ERRO}⚠ Cliente banido voltou!{COR_RESET}")
        while True:
            op = input("Expulsar? (s/n): ").lower()
            if op in ("s","n"):
                break
        if op == "s":
            print("Cliente expulso!")
            return vendidos, roubos, dinheiro_recebido, caixa, clientes_insatisfeitos
        else:
            e_ladrao = True
            chance_roubo = min(chance_roubo + 30, 90)

    # Escolher produtos aleatórios
    n_produtos = random.randint(1,3)
    lista_compra = []

    for _ in range(n_produtos):
        idx = random.randint(0, len(produtos)-1)
        nome_p, preco, stock = produtos[idx]
        if stock <= 0:
            continue
        quantidade = 1
        if preco < 1:
            quantidade = random.randint(2,5)
        lista_compra.append((idx, nome_p, preco, quantidade, stock))

    # Se nenhum produto disponível
    if not lista_compra:
        print("Cliente não comprou nada.")
        return vendidos, roubos, dinheiro_recebido, caixa, clientes_insatisfeitos

    # Mostrar compra
    linha()
    print("🛒 Cliente vai comprar os seguintes produtos:")
    total = 0
    for idx, nome_p, preco, quantidade, stock in lista_compra:
        print(f"{nome_p} x{quantidade} | Preço unitário: {preco:.3f}€ | Stock: {stock}")
        total += round(preco * quantidade, 3)
    total = round(total, 3)
    print(f"Total: {total:.3f}€")
    linha()

    # Perguntar se quer confrontar
    while True:
        conf = input("Confrontar cliente? (s/n): ").lower()
        if conf in ("s","n"):
            break

    # Se confrontar
    if conf == "s":
        if e_ladrao:
            print("✔ Era ladrão! Pagou e foi banido.")
            clientes_banidos.append((nome, idade, sexo, categoria, True, True, False, chance_roubo))
            for idx, nome_p, preco, quantidade, stock in lista_compra:
                produtos[idx] = (nome_p, preco, stock-quantidade)
                vendidos += quantidade
                roubos += 1
            caixa += total
            dinheiro_recebido += total
            return vendidos, roubos, dinheiro_recebido, caixa, clientes_insatisfeitos
        else:
            print("❌ Não era ladrão! Foi embora chateado.")
            clientes_insatisfeitos += 1
            return vendidos, roubos, dinheiro_recebido, caixa, clientes_insatisfeitos

    # Se não confrontar e for ladrão
    if e_ladrao:
        print("💀 Roubou produtos!")
        for idx, nome_p, preco, quantidade, stock in lista_compra:
            produtos[idx] = (nome_p, preco, stock-quantidade)
            roubos += 1
            clientes_insatisfeitos += 1
        return vendidos, roubos, dinheiro_recebido, caixa, clientes_insatisfeitos

    # Pagamento normal
    extra = random.choice([0, 0.1, 0.2, 0.3, 0.5, 1, 2, 5])
    valor_cliente = round(total + extra, 3)
    troco_correto = round(valor_cliente - total, 3)

    print(f"Cliente deu: {valor_cliente:.3f}€")

    while True:
        try:
            troco = round(float(input("Quanto dás de troco? ")), 3)
            break
        except:
            print("Valor inválido.")

    if troco > troco_correto:
        print("Deste troco a mais!")
        if random.randint(1,100) <= 50:
            caixa -= troco
        else:
            caixa -= troco_correto
    elif troco < troco_correto:
        print("Deste troco a menos!")
        if random.randint(1,100) <= 50:
            clientes_insatisfeitos += 1
            caixa -= troco
        else:
            caixa -= troco_correto
    else:
        print("Troco correto!")
        caixa -= troco_correto

    for idx, nome_p, preco, quantidade, stock in lista_compra:
        produtos[idx] = (nome_p, preco, stock-quantidade)
        vendidos += quantidade

    caixa += valor_cliente
    dinheiro_recebido += total

    return vendidos, roubos, dinheiro_recebido, caixa, clientes_insatisfeitos
