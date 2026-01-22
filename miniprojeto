# Definição de cores para o terminal
g = '\033[92m'#verde
y = '\033[93m'#amarelo
v = '\033[91m'#vermelho
a = '\033[94m'#azul
n = '\033[1m'#negrito
r = '\033[0m' # Volta à cor normal
# Pergunta quantas notas o utilizador quer inserir

while True:
    try:
        quantidade = int(input(f"{a}Quantas notas quer inserir?{r} "))
        if quantidade <= 0:
            print(f"{v}Insira um número inteiro maior que zero.{r}")
        else:
            break
    except ValueError:
        print(f"{v}Erro: tem de inserir um número inteiro.{r}")



notas = []

# Ler as notas e guardar na lista
for i in range(quantidade):
    while True:
        try:
            nota = float(input(f"{a}Insira a nota:{r}, {i + 1}:"))
            if nota< 0 or nota > 100:
                print(f"{v}Insira um número inteiro maior que zero.{r}")
            else:
                notas.append(nota)
                break
        except ValueError:
        print("{v}Erro: tem de inserir um número.{r}")

# Menu de opções
while True:
    print(f"{a}Notes.py:{r}")
    print(f"{g}1 - Média das notas{r}")
    print(f"{g}2 - Nota máxima{r}")
    print(f"{g}3 - Nota mínima{r}")
    print(f"{v}4 - Sair{r}")

    opcao = input(f"{n}Escolha uma opção:{r} ")

    if opcao == "1":
        media = sum(notas) / len(notas)
        print(f"{n}Média das notas:{r}", media)

    elif opcao == "2":
        print(f"{v}Nota máxima:{r}", max(notas))

    elif opcao == "3":
        print(f"{a}Nota mínima:7", min(notas))

    elif opcao == "4":
        print(f"{r}Programa terminado.{r}")
        break

    else:
        print(f"{r}Opção inválida. Tente novamente.{r}")
