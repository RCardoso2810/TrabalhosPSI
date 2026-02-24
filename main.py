# ==========================================
# IMPORTAÇÕES
# ==========================================

from dados import dinheiro_inicial, produtos
from clientes import gerar_cliente
from logica import mostrar_cliente, processar_compra, linha
import random

# ==========================================
# CORES DO TERMINAL
# ==========================================

COR_RESET = '\033[0m'
COR_TITULO = '\033[95m'
COR_SUCESSO = '\033[92m'
COR_ERRO = '\033[91m'
COR_AVISO = '\033[93m'
COR_INFO = '\033[96m'

# ==========================================
# LISTA DE UPGRADES
# ==========================================

upgrades = [
    ("Segurança Extra", 20, "reduz_roubo"),
    ("Promoção Produtos", 15, "mais_vendas"),
    ("Estoque Ampliado", 25, "mais_stock"),
    ("Caixa Automático", 30, "mais_caixa")
]

efeitos_ativos = []

# ==========================================
# ESCOLHER DIFICULDADE
# ==========================================

def escolher_dificuldade():
    while True:
        linha()
        print(f"{COR_TITULO}ESCOLHA A DIFICULDADE{COR_RESET}")
        print(f"{COR_INFO}1 - Fácil (3 rondas)")
        print(f"2 - Médio (5 rondas)")
        print(f"3 - Difícil (10 rondas){COR_RESET}")
        op = input("Escolha: ")
        if op == "1": return 3
        if op == "2": return 5
        if op == "3": return 10

# ==========================================
# MOSTRAR UPGRADES
# ==========================================

def mostrar_upgrades(caixa):
    linha()
    print(f"{COR_TITULO}UPGRADES DISPONÍVEIS{COR_RESET}")
    for i, (nome, preco, efeito) in enumerate(upgrades):
        cor = COR_SUCESSO if caixa >= preco else COR_ERRO
        print(f"{i+1} - {nome} | Custo: {cor}{preco}€{COR_RESET}")
    print("0 - Nenhum")
    linha()

# ==========================================
# APLICAR UPGRADE
# ==========================================

def aplicar_upgrade(caixa, lista_produtos, efeitos_ativos):
    while True:
        mostrar_upgrades(caixa)
        escolha = input("Escolhe upgrade ou 0 para continuar: ")
        if escolha.isdigit():
            escolha = int(escolha)
            if escolha == 0:
                break
            elif 1 <= escolha <= len(upgrades):
                nome, preco, efeito = upgrades[escolha-1]
                if caixa >= preco:
                    caixa -= preco
                    efeitos_ativos.append(efeito)
                    print(f"{COR_SUCESSO}✔ Upgrade {nome} adquirido!{COR_RESET}")
                    break
                else:
                    print(f"{COR_ERRO}✖ Caixa insuficiente para {nome}!{COR_RESET}")

    if "mais_stock" in efeitos_ativos:
        nova_lista = []
        for nome_p, preco_p, stock in lista_produtos:
            nova_lista.append((nome_p, preco_p, stock+5))
        lista_produtos[:] = nova_lista

    return caixa

# ==========================================
# FUNÇÃO PRINCIPAL
# ==========================================

def main():

    rondas = escolher_dificuldade()
    caixa = dinheiro_inicial
    lista_produtos = list(produtos)
    clientes_banidos = []
    lucro_total = 0

    for ronda in range(1, rondas+1):

        linha()
        print(f"{COR_TITULO}📊 RONDA {ronda}{COR_RESET}")
        linha()

        numero_clientes = max(1, 3 + ronda)

        evento = random.randint(1,100)
        if evento <= 20:
            print(f"{COR_AVISO}📉 Crise económica! -2 clientes{COR_RESET}")
            numero_clientes = max(1, numero_clientes-2)
        elif evento <= 35:
            print(f"{COR_SUCESSO}📈 Dia movimentado! +3 clientes{COR_RESET}")
            numero_clientes += 3
        elif evento <= 45:
            print(f"{COR_ERRO}💸 Multa 20€{COR_RESET}")
            caixa -= 20
        elif evento <= 55:
            print(f"{COR_SUCESSO}🎁 Bónus fornecedor +15€{COR_RESET}")
            caixa += 15

        # ==============================
        # UPGRADES ENTRE RONDAS
        # ==============================
        if ronda > 1:
            caixa = aplicar_upgrade(caixa, lista_produtos, efeitos_ativos)

            # ==============================
            # COMPRA DE STOCK ENTRE RONDAS
            # ==============================
            while True:
                linha()
                print(f"{COR_TITULO}📦 Comprar Stock?{COR_RESET}")
                print("1 - Sim")
                print("0 - Não")

                op_stock = input("Escolha: ")

                if op_stock == "0":
                    break

                elif op_stock == "1":

                    linha()
                    print(f"{COR_INFO}Produtos disponíveis:{COR_RESET}")
                    for i, (nome_p, preco_p, stock_p) in enumerate(lista_produtos):
                        print(f"{i+1} - {nome_p} | Preço: {preco_p}€ | Stock atual: {stock_p}")

                    escolha_prod = input("Escolhe produto (número): ")

                    if escolha_prod.isdigit():
                        escolha_prod = int(escolha_prod) - 1

                        if 0 <= escolha_prod < len(lista_produtos):

                            nome_p, preco_p, stock_p = lista_produtos[escolha_prod]

                            quantidade = input("Quantidade a comprar: ")

                            if quantidade.isdigit():
                                quantidade = int(quantidade)

                                custo = round((preco_p * 0.5) * quantidade, 2)

                                if caixa >= custo:
                                    caixa -= custo
                                    lista_produtos[escolha_prod] = (nome_p, preco_p, stock_p + quantidade)
                                    print(f"{COR_SUCESSO}✔ Compraste {quantidade}x {nome_p}!{COR_RESET}")
                                    print(f"{COR_AVISO}Custo: {custo}€{COR_RESET}")
                                else:
                                    print(f"{COR_ERRO}✖ Dinheiro insuficiente!{COR_RESET}")

        vendidos_ronda = 0
        roubos_ronda = 0
        dinheiro_ronda = 0
        clientes_insatisfeitos_ronda = 0

        for _ in range(numero_clientes):

            cliente = gerar_cliente(ronda)

            if "reduz_roubo" in efeitos_ativos:
                cliente = list(cliente)
                cliente[7] = max(cliente[7]-15, 0)
                cliente = tuple(cliente)

            mostrar_cliente(cliente)

            v, r, d, caixa_temp, ins = processar_compra(cliente, lista_produtos, 0, clientes_banidos)

            if "mais_caixa" in efeitos_ativos:
                d += 2

            vendidos_ronda += v
            roubos_ronda += r
            dinheiro_ronda += d
            clientes_insatisfeitos_ronda += ins

        caixa += dinheiro_ronda

        stock_total = sum(prod[2] for prod in lista_produtos)
        if stock_total <= 0:
            linha()
            print(f"{COR_ERRO}💀 GAME OVER! Ficou sem stock!{COR_RESET}")
            break

        if clientes_insatisfeitos_ronda > numero_clientes/2:
            linha()
            print(f"{COR_ERRO}💀 GAME OVER! Muitos clientes insatisfeitos.{COR_RESET}")
            break

        if roubos_ronda > numero_clientes/3:
            linha()
            print(f"{COR_ERRO}💀 GAME OVER! Muitos clientes roubaram.{COR_RESET}")
            break

        lucro_total += dinheiro_ronda

        linha()
        print(f"{COR_SUCESSO}💰 Caixa atual: {round(caixa,2)}€{COR_RESET}")
        print(f"{COR_INFO}📦 Produtos vendidos nesta ronda: {vendidos_ronda}")
        print(f"🤕 Clientes insatisfeitos: {clientes_insatisfeitos_ronda}")
        print(f"🛍️ Roubos nesta ronda: {roubos_ronda}{COR_RESET}")

    linha()
    print(f"{COR_TITULO}🏁 FIM DO JOGO{COR_RESET}")
    print(f"{COR_SUCESSO}Lucro total: {round(lucro_total,2)}€")
    print(f"{COR_INFO}Dinheiro final: {round(caixa,2)}€{COR_RESET}")

    if efeitos_ativos:
        print(f"{COR_TITULO}🔧 Upgrades comprados: {', '.join(efeitos_ativos)}{COR_RESET}")

    linha()

if __name__ == "__main__":
    main()
