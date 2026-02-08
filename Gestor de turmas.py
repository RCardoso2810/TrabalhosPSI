# ================== TURMA 10-1ºA ==================

RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
CIANO = "\033[96m"

turma = [[], []]


def limpar_tela():
    print("\n" * 50)


def imagem_menu():
    print(CIANO + """
==============================
       TURMA 10-1ºA
==============================
""" + RESET)


def validar_nome(texto):
    return texto.istitle()


def validar_idade(idade):
    return 0 <= idade <= 100


def organizar_turnos():
    todas = turma[0] + turma[1]
    todas.sort(key=lambda x: (x["sobrenome"], x["nome"]))

    turma[0].clear()
    turma[1].clear()

    for i, pessoa in enumerate(todas):
        if i % 2 == 0:
            turma[0].append(pessoa)
        else:
            turma[1].append(pessoa)


def adicionar_pessoa():
    while True:
        nome = input(AZUL + "Nome: " + RESET)
        if validar_nome(nome):
            break
        print(VERMELHO + "Nome inválido (primeira letra deve ser maiúscula)." + RESET)

    while True:
        sobrenome = input(AZUL + "Sobrenome: " + RESET)
        if validar_nome(sobrenome):
            break
        print(VERMELHO + "Sobrenome inválido (primeira letra deve ser maiúscula)." + RESET)

    while True:
        try:
            idade = int(input(AZUL + "Idade: " + RESET))

            if idade < 0:
                print(VERMELHO + "Idade não pode ser negativa." + RESET)
            elif idade > 100:
                print(VERMELHO + "Idade excedida (máximo 100 anos)." + RESET)
            else:
                break

        except:
            print(VERMELHO + "Idade inválida. Digite um número." + RESET)

    pessoa = {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade
    }

    turma[0].append(pessoa)
    organizar_turnos()
    print(VERDE + "Pessoa adicionada com sucesso!" + RESET)


def remover_pessoa():
    nome = input(AMARELO + "Nome da pessoa a remover: " + RESET)

    for turno in turma:
        for pessoa in turno:
            if pessoa["nome"] == nome:
                turno.remove(pessoa)
                organizar_turnos()
                print(VERDE + "Pessoa removida!" + RESET)
                return

    print(VERMELHO + "Pessoa não encontrada." + RESET)


def mostrar_turma():
    print(CIANO + "\n--- TURNO 1 ---" + RESET)
    for p in turma[0]:
        print(f'{p["nome"]} {p["sobrenome"]} - {p["idade"]} anos')

    print(CIANO + "\n--- TURNO 2 ---" + RESET)
    for p in turma[1]:
        print(f'{p["nome"]} {p["sobrenome"]} - {p["idade"]} anos')


def procurar_pessoa():
    todas = turma[0] + turma[1]

    if not todas:
        print(VERMELHO + "A turma está vazia." + RESET)
        return

    print(CIANO + """
Procurar por:
1 - Nome
2 - Sobrenome
3 - Idade
""" + RESET)

    opcao = input("Escolha uma opção: ")
    encontrados = []

    if opcao == "1":
        nome = input("Nome a procurar: ")
        encontrados = [p for p in todas if p["nome"] == nome]

    elif opcao == "2":
        sobrenome = input("Sobrenome a procurar: ")
        encontrados = [p for p in todas if p["sobrenome"] == sobrenome]

    elif opcao == "3":
        try:
            idade = int(input("Idade a procurar: "))
            encontrados = [p for p in todas if p["idade"] == idade]
        except:
            print(VERMELHO + "Idade inválida." + RESET)
            return

    else:
        print(VERMELHO + "Opção inválida." + RESET)
        return

    if encontrados:
        print(VERDE + "\nPessoas encontradas:" + RESET)
        for p in encontrados:
            print(f'{p["nome"]} {p["sobrenome"]} - {p["idade"]} anos')
    else:
        print(AMARELO + "Nenhuma pessoa encontrada." + RESET)


def menu():
    while True:
        limpar_tela()
        imagem_menu()
        print(AZUL + """
1 - Adicionar pessoa
2 - Remover pessoa
3 - Mostrar turma
4 - Procurar pessoa
0 - Sair
""" + RESET)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_pessoa()
            input("\nEnter para continuar...")
        elif opcao == "2":
            remover_pessoa()
            input("\nEnter para continuar...")
        elif opcao == "3":
            mostrar_turma()
            input("\nEnter para continuar...")
        elif opcao == "4":
            procurar_pessoa()
            input("\nEnter para continuar...")
        elif opcao == "0":
            print(AMARELO + "Saindo..." + RESET)
            break
        else:
            print(VERMELHO + "Opção inválida." + RESET)
            input("\nEnter para continuar...")


menu()
