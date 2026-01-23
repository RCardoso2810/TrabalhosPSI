# Definição de cores para o terminal
g = '\033[92m'  # verde
y = '\033[93m'  # amarelo
v = '\033[91m'  # vermelho
a = '\033[94m'  # azul
n = '\033[1m'  # negrito
r = '\033[0m'  # Volta à cor normal

# Lista para armazenar o histórico
historico_frases = []


def transformar_texto(texto):
    # Criamos um dicionário com as substituições desejadas
    tabela_substituicao = {
        'a': '@', 'A': '9',
        'b': '8', 'B': '8',
        'c': '(', 'C': '(',
        'd': ')', 'D': ')',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        ' ': '_'
    }

    # Criamos uma tabela de tradução que o Python entende
    tabela = str.maketrans(tabela_substituicao)

    # Aplicamos a tradução ao texto e retornamos o resultado
    return texto.translate(tabela)


def palavra_len(frase):
    frasel = len(frase)
    if frasel < 8:
        print(f"{y}A tua passe deve conter pelo menos 8 caracteres{r}")

        return False
    else:
        return True


def exibir_menu():

    while True:
        frase = input("escreva sua palavra passe:")


        if palavra_len(frase):
            # Adiciona a frase ao histórico se for válida
            historico_frases.append(frase)

            contrario = frase[::-1]
            frase_f = str(00) + frase + str(00) + "@"
            frase_m = transformar_texto(frase)
            frase_fo = transformar_texto(contrario)
            print(f"{y}---{r}{g}Criador de passes{r} {y}---{r}")
            print(f"{g}1.Passe Fraca{r}")
            print(f"{y}2.Passe média{r}")
            print(f"{v}3. Passe Forte{r}")
            print(f"{y}0. Sair{r}")

            opcao = input(f"{g}Escolha uma opção:{r}")

            if opcao == "0":
                print(f"{v}A sair até a próxima {r}")
                break
            elif opcao == "1":
                print(frase_f)
                historico_frases.append(frase_f)
            elif opcao == "2":
                print(frase_m)
                historico_frases.append(frase_m)
            elif opcao == "3":
                print(frase_fo)
                historico_frases.append(frase_fo)
            elif opcao == "89":
                print(f"\n{a}--- Registros de Frases ---{r}")
                if not historico_frases:
                    print("Nenhum registro encontrado no sistema.")
                else:
                    for i, registro in enumerate(historico_frases, 1):
                        print(f"{i}. {registro}")
                print(f"{a}---------------------------{r}\n")
                while True:
                    voltar=input("escreva voltar para ir para o menu")
                    if voltar == "menu":
                        break
            else:
                while True:
                    print("Essa escolha é inválida")
                    voltar = input("escreva voltar para ir para o menu")
                    if voltar == "menu":
                        break

# Para correr o programa
exibir_menu()




