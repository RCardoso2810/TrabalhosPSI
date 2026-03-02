from gestor import GestorEvento
from evento import Evento


def validar_nome():
    while True:
        nome = input("Nome do evento (apenas letras): ")
        if nome.isalpha(): return nome
        print("Erro: Use apenas letras.")


def validar_data():
    while True:
        txt = input("Data (DD|MM|AAAA): ")
        p = txt.split("|")
        if len(p) == 3 and all(i.isdigit() for i in p):
            d, m, a = map(int, p)
            if 1 <= d <= 31 and 1 <= m <= 12: return (d, m, a)
        print("Erro: Use o formato DD|MM|AAAA.")


def main():
    gestor = GestorEvento()

    while True:
        print(f"\n[ HOJE: {gestor.dia_atual_sistema.strftime('%d/%m/%Y')} ]")
        print("1 - Criar Evento")
        print("2 - Ver Eventos")
        print("3 - Configurar Turmas")
        print("4 - Adicionar Aluno / Pagamentos")
        print("5 - Estatísticas e Turmas")
        print("6 - Avançar no Tempo")
        print("7 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            nome = validar_nome()
            data = validar_data()
            try:
                preco = float(input("Preço: "))
                gestor.criar_evento(Evento(nome, data, 0, 0, preco))
            except:
                print("Preço inválido.")

        elif opcao == "2":
            gestor.listar_eventos()

        elif opcao == "3":
            gestor.configurar_turmas_evento()

        elif opcao == "4":
            if not gestor.evento_atual: print("Crie evento!"); continue
            print("1. Novo Aluno | 2. Pagamento | 3. Desistência")
            sub = input("Opção: ")
            if sub == "1":
                if not gestor.turmas: print("Configure turmas primeiro!"); continue
                n = input("Nome: ")
                for i, t in enumerate(gestor.turmas): print(i, "-", t)
                gestor.adicionar_aluno(n, int(input("Turma: ")))
            elif sub == "2":
                for i, a in enumerate(gestor.alunos): print(i, "-", a.nome)
                idx = int(input("ID: "))
                gestor.alunos[idx].adicionar_pagamento(float(input("Valor: ")))
            elif sub == "3":
                for i, a in enumerate(gestor.alunos): print(i, "-", a.nome)
                idx = int(input("ID: "))
                gestor.alunos[idx].marcar_presenca(False)

        elif opcao == "5":
            gestor.ver_estatisticas()

        elif opcao == "6":
            dias = int(input("Quantos dias avançar? "))
            gestor.avancar_tempo(dias)

        elif opcao == "7":
            break


if __name__ == "__main__":
    main()
  
