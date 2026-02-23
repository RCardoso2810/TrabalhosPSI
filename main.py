# main.py
from dados import dinheiro_inicial, produtos
from clientes import gerar_cliente
from logica import mostrar_cliente, processar_compra

# Cores
COR_TITULO = '\033[35m'
COR_DESTAQUE = '\033[36m'
COR_SUCESSO = '\033[32m'
COR_ERRO = '\033[31m'
COR_AVISO = '\033[33m'
COR_TEXTO = '\033[37m'
COR_RESET = '\033[0m'

def escolher_dificuldade():
    while True:
        print(f"{COR_DESTAQUE}Escolhe dificuldade:{COR_RESET}")
        print(f"{COR_SUCESSO}1. Fácil (3 rondas){COR_RESET}")
        print(f"{COR_DESTAQUE}2. Médio (5 rondas){COR_RESET}")
        print(f"{COR_ERRO}3. Difícil (10 rondas){COR_RESET}")
        opcao = input("Opção (1/2/3): ")
        if opcao == "1":
            return 3
        elif opcao == "2":
            return 5
        elif opcao == "3":
            return 10
        else:
            print(f"{COR_AVISO}⚠ Escolha inválida{COR_RESET}")

def mostrar_stock(produtos):
    print(f"\n{COR_DESTAQUE}📦 Stock atual dos produtos:{COR_RESET}")
    for p in produtos:
        print(f"{COR_TEXTO}- {p[0]}: {p[2]} unidades{COR_RESET}")

def comprar_estoque(caixa, produtos):
    print(f"\n{COR_DESTAQUE}🛒 Comprar mais stock{COR_RESET}")
    mostrar_stock(produtos)
    print(f"{COR_TEXTO}Dinheiro disponível: {caixa} €{COR_RESET}")
    while True:
        try:
            gasto = int(input("Quanto gastar em estoque? (100/200/300/400 ou 0 para não comprar): "))
            if gasto in (0,100,200,300,400):
                if gasto > caixa:
                    print(f"{COR_ERRO}⚠ Dinheiro insuficiente!{COR_RESET}")
                    continue
                break
        except:
            print(f"{COR_AVISO}⚠ Valor inválido{COR_RESET}")
    if gasto == 0:
        return caixa, produtos

    nova_lista = []
    total_preco = sum([p[1] for p in produtos])
    for nome, preco, stock in produtos:
        # Quantidade adicionada proporcional ao preço e ao valor gasto
        n_add = int((preco / total_preco) * gasto / preco)
        nova_lista.append((nome, preco, stock + n_add))

    caixa -= gasto
    print(f"{COR_SUCESSO}✔ Stock atualizado após compra.{COR_RESET}")
    mostrar_stock(nova_lista)
    return caixa, nova_lista

def main():
    total_rondas = escolher_dificuldade()
    caixa = dinheiro_inicial
    lista_produtos = list(produtos)
    clientes_banidos = []

    total_vendas = 0
    total_roubos = 0

    for ronda in range(1, total_rondas+1):
        print(f"\n{COR_DESTAQUE}=============================={COR_RESET}")
        print(f"{COR_TITULO}RONDA {ronda}{COR_RESET}")
        print(f"{COR_DESTAQUE}=============================={COR_RESET}")

        vendidos = 0
        roubos = 0
        dinheiro_ronda = 0

        numero_clientes = 3 + ronda

        for _ in range(numero_clientes):
            cliente = gerar_cliente(ronda)
            mostrar_cliente(cliente)
            v, r, d, caixa, cliente = processar_compra(cliente, lista_produtos, caixa)
            vendidos += v
            roubos += r
            dinheiro_ronda += d
            if cliente[5]:
                clientes_banidos.append(cliente)

        total_vendas += vendidos
        total_roubos += roubos

        print(f"\n{COR_DESTAQUE}--- ESTATÍSTICAS DA RONDA ---{COR_RESET}")
        print(f"{COR_SUCESSO}Itens vendidos:{COR_RESET} {vendidos}")
        print(f"{COR_ERRO}Tentativas de roubo:{COR_RESET} {roubos}")
        print(f"{COR_SUCESSO}Dinheiro ganho nesta ronda:{COR_RESET} {dinheiro_ronda} €")
        print(f"{COR_DESTAQUE}Dinheiro total na caixa:{COR_RESET} {caixa} €")

        if all(p[2]==0 for p in lista_produtos):
            print(f"{COR_ERRO}\n⚠ FALÊNCIA! Sem stock para continuar.{COR_RESET}")
            return

        caixa, lista_produtos = comprar_estoque(caixa, lista_produtos)

        # Condições para perder
        if vendidos < numero_clientes / 2 or roubos > numero_clientes / 3:
            print(f"\n{COR_ERRO}GAME OVER! Não passaste de nível.{COR_RESET}")
            print(f"{COR_TEXTO}Estatísticas totais até agora:{COR_RESET}")
            print(f"{COR_SUCESSO}Vendas totais: {total_vendas}{COR_RESET}")
            print(f"{COR_ERRO}Roubos totais: {total_roubos}{COR_RESET}")
            return

    print(f"\n{COR_SUCESSO}YOU WIN! 🎉{COR_RESET}")
    print(f"{COR_TEXTO}Estatísticas finais:{COR_RESET}")
    print(f"{COR_SUCESSO}Vendas totais: {total_vendas}{COR_RESET}")
    print(f"{COR_ERRO}Roubos totais: {total_roubos}{COR_RESET}")
    print(f"{COR_DESTAQUE}Dinheiro final na caixa: {COR_RESET}{caixa} €")

if __name__ == "__main__":
    main()
