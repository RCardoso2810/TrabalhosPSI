# logica.py
import random

# Cores
COR_RESET = '\033[0m'
COR_TITULO = '\033[35m'
COR_DESTAQUE = '\033[36m'
COR_SUCESSO = '\033[32m'
COR_ERRO = '\033[31m'
COR_AVISO = '\033[33m'
COR_TEXTO = '\033[37m'

def mostrar_cliente(cliente):
    nome, idade, sexo, categoria, e_ladrao, banido, chateado, chance_roubo = cliente
    print(f"\n{COR_DESTAQUE}--- CLIENTE ---{COR_RESET}")
    print(f"{COR_TEXTO}Nome:{COR_RESET} {nome}")
    print(f"{COR_TEXTO}Idade:{COR_RESET} {idade}")
    print(f"{COR_TEXTO}Sexo:{COR_RESET} {sexo}")
    print(f"{COR_TEXTO}Categoria:{COR_RESET} {categoria}")
    if banido:
        print(f"{COR_ERRO}⚠ Cliente banido anteriormente.{COR_RESET}")
    if chateado:
        print(f"{COR_AVISO}⚠ Cliente chateado, não volta mais.{COR_RESET}")
    print(f"{COR_AVISO}💀 Chance de roubo: {chance_roubo}%{COR_RESET}")

def selecionar_produto(produtos):
    idx = random.randint(0, len(produtos)-1)
    nome, preco, stock = produtos[idx]
    return idx, nome, preco, stock

def processar_compra(cliente, produtos, caixa):
    nome, idade, sexo, categoria, e_ladrao, banido, chateado, chance_roubo = cliente
    vendidos = 0
    roubos = 0
    dinheiro_recebido = 0

    if chateado:
        return vendidos, roubos, dinheiro_recebido, caixa, cliente

    n_produtos = random.randint(1,3)  # Cliente quer comprar 1-3 produtos
    for _ in range(n_produtos):
        idx, p_nome, preco, stock = selecionar_produto(produtos)
        if stock <= 0:
            print(f"{COR_ERRO}⚠ Produto sem stock: {p_nome}{COR_RESET}")
            continue

        print(f"{COR_TEXTO}Cliente quer comprar: {COR_SUCESSO}{p_nome}{COR_RESET} (Preço: {COR_DESTAQUE}{preco}€{COR_RESET})")

        while True:
            confrontar = input(f"{COR_DESTAQUE}Queres confrontar o cliente? (s/n): {COR_RESET}").lower()
            if confrontar in ("s","n"):
                break
            print(f"{COR_AVISO}⚠ Resposta inválida. Escreve 's' ou 'n'.{COR_RESET}")

        if confrontar == "s":
            if e_ladrao:
                print(f"{COR_SUCESSO}✔ Confronto correto! Cliente paga e é banido.{COR_RESET}")
                caixa += preco
                dinheiro_recebido += preco
                produtos[idx] = (p_nome, preco, stock-1)
                vendidos += 1
                cliente = (nome, idade, sexo, categoria, False, True, False, chance_roubo)
                roubos += 1
            else:
                print(f"{COR_ERRO}❌ Cliente não era ladrão, ficou chateado e vai embora.{COR_RESET}")
                cliente = (nome, idade, sexo, categoria, False, False, True, chance_roubo)
            continue

        if e_ladrao:
            print(f"{COR_ERRO}💀 Cliente roubou o produto e foi embora sem pagar!{COR_RESET}")
            produtos[idx] = (p_nome, preco, stock-1)
            cliente = (nome, idade, sexo, categoria, True, False, True, chance_roubo)
            roubos += 1
            continue

        while True:
            try:
                valor_cliente = float(input(f"{COR_TEXTO}Cliente dá quanto? (Preço: {preco}€): {COR_RESET}"))
                break
            except:
                print(f"{COR_AVISO}⚠ Escreve um número válido.{COR_RESET}")

        if valor_cliente < preco:
            while True:
                opc = input(f"{COR_AVISO}Valor insuficiente. Aceitar parcial, negar ou corrigir? (a/n/c): {COR_RESET}").lower()
                if opc in ("a","n","c"):
                    break
                print(f"{COR_AVISO}⚠ Opção inválida{COR_RESET}")
            if opc == "n":
                print(f"{COR_ERRO}❌ Compra negada{COR_RESET}")
                continue
            elif opc == "a":
                dinheiro_recebido += valor_cliente
                caixa += valor_cliente
                produtos[idx] = (p_nome, preco, stock-1)
                vendidos += 1
                continue
            elif opc == "c":
                valor_cliente = preco

        while True:
            try:
                troco = float(input(f"{COR_TEXTO}Quanto dás de troco? (Preço: {preco}, cliente deu: {valor_cliente}): {COR_RESET}"))
                break
            except:
                print(f"{COR_AVISO}⚠ Escreve um número válido.{COR_RESET}")

        troco_correto = valor_cliente - preco
        if troco != troco_correto:
            print(f"{COR_ERRO}⚠ Troco incorreto! Correto seria {troco_correto:.2f}€{COR_RESET}")
            chance = random.randint(1,100)
            if chance <= 50:
                print(f"{COR_ERRO}❌ Cliente foi embora com o troco errado! Perdes o dinheiro extra.{COR_RESET}")
                caixa -= troco
            else:
                print(f"{COR_DESTAQUE}⌛ Cliente espera pelo troco correto.{COR_RESET}")
                troco = troco_correto
                print(f"{COR_SUCESSO}✔ Troco correto dado: {troco:.2f}€{COR_RESET}")
                caixa -= troco
        else:
            caixa -= troco
            print(f"{COR_SUCESSO}✔ Troco correto entregue: {troco:.2f}€{COR_RESET}")

        dinheiro_recebido += preco
        caixa += preco
        produtos[idx] = (p_nome, preco, stock-1)
        vendidos += 1

    return vendidos, roubos, dinheiro_recebido, caixa, cliente
