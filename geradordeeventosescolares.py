from gestor import GestorEvento
from evento import Evento
from datetime import date


def validar_data(msg):
    while True:
        txt = input(f"{msg} (DD|MM|AAAA) ou '0' para voltar: ")

        if txt == '0':
            return '0'

        p = txt.split("|")

        if len(p) == 3 and all(i.isdigit() for i in p):
            d, m, a = map(int, p)

            # LIMITADOR DO MÊS
            if m < 1 or m > 12:
                print("\033[91mErro: O mês deve estar entre 1 e 12.\033[0m")
                continue

            # LIMITADOR DO DIA
            if d < 1 or d > 31:
                print("\033[91mErro: O dia deve estar entre 1 e 31.\033[0m")
                continue

            return (d, m, a)

        print("\033[91mErro: Use o formato DD|MM|AAAA.\033[0m")


def main():
    gestor = GestorEvento()

    while True:
        print(f"\n\033[96m[ HOJE: {gestor.dia_atual_sistema.strftime('%d/%m/%Y')} ]\033[0m")
        print("1 - Criar Evento")
        print("2 - Ver Eventos")
        print("3 - Configurar Turmas")
        print("4 - Adicionar Aluno / Pagamentos")
        print("5 - Estatísticas e Turmas")
        print("6 - Avançar no Tempo")
        print("7 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = input("Nome do evento (0 para voltar): ").strip().upper()
            if nome == '0': continue
            data_e = validar_data("Data do evento")
            if data_e == '0': continue

            # NOVA VALIDAÇÃO: impedir evento antes de hoje
            data_evento_obj = date(data_e[2], data_e[1], data_e[0])
            if data_evento_obj < gestor.dia_atual_sistema:
                print("\033[91mErro: A data do evento não pode ser anterior ao dia atual!\033[0m")
                continue
            data_l = validar_data("Data limite de pagamento")
            if data_l == '0': continue

            # Validação: Data limite não pode ser depois do evento
            if date(data_l[2], data_l[1], data_l[0]) > date(data_e[2], data_e[1], data_e[0]):
                print("\033[91mErro: A data limite não pode ser depois do evento!\033[0m")
                continue
            try:
                preco = float(input("Preço: "))
                gestor.criar_evento(Evento(nome, data_e, data_l, preco))
            except:
                print("\033[91mPreço inválido.\033[0m")

        elif opcao == "2":
            gestor.listar_eventos()

        elif opcao == "3":
            gestor.configurar_turmas_evento()

        elif opcao == "4":
            if not gestor.evento_atual: print("Crie evento!"); continue
            print("1. Novo Aluno | 2. Pagamento | 3. Desistência | 0. Voltar")
            sub = input("Opção: ")
            if sub == "0": continue
            try:
                if sub == "1":
                    if not gestor.turmas: print("Configure turmas primeiro!"); continue
                    n = input("Nome (0 para voltar): ").strip().upper()
                    if n == '0': continue
                    lt = sorted(list(gestor.turmas))
                    for i, t in enumerate(lt): print(i, "-", t)
                    gestor.adicionar_aluno(n, int(input("Turma: ")))
                elif sub == "2":
                    for i, a in enumerate(gestor.alunos): print(i, "-", a.nome)
                    idx = int(input("ID: "))
                    gestor.alunos[idx].adicionar_pagamento(float(input("Valor: ")))
                elif sub == "3":
                    for i, a in enumerate(gestor.alunos): print(i, "-", a.nome)
                    idx = int(input("ID: "))
                    gestor.alunos[idx].marcar_presenca(False)
            except:
                print("\033[91mErro nos dados inseridos.\033[0m")

        elif opcao == "5":
            gestor.ver_estatisticas()

        elif opcao == "6":
            try:
                dias = int(input("Quantos dias avançar? (0 para voltar): "))
                if  dias != 0:gestor.avancar_tempo(dias)
            except:
                print("\033[91mErro: Digite um número.\033[0m")

        elif opcao == "7":
            break


if __name__ == "__main__":
    main()
