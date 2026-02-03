# ===== Estilos =====
n  = '\033[1m'    # negrito
d  = '\033[2m'    # fraco
i  = '\033[3m'    # itálico
u  = '\033[4m'    # sublinhado
p  = '\033[5m'    # piscando (nem todo terminal suporta)
r  = '\033[0m'    # reset (volta ao normal)

# ===== Cores padrão (texto) =====
preto   = '\033[30m'
vermelho= '\033[31m'
verde   = '\033[32m'
amarelo = '\033[33m'
azul    = '\033[34m'
roxo    = '\033[35m'
ciano   = '\033[36m'
branco  = '\033[37m'

# ===== Cores claras (bright) =====
preto_c   = '\033[90m'
vermelho_c= '\033[91m'
verde_c   = '\033[92m'
amarelo_c = '\033[93m'
azul_c    = '\033[94m'
roxo_c    = '\033[95m'
ciano_c   = '\033[96m'
branco_c  = '\033[97m'

# ===== Fundo (background) =====
bg_preto   = '\033[40m'
bg_vermelho= '\033[41m'
bg_verde   = '\033[42m'
bg_amarelo = '\033[43m'
bg_azul    = '\033[44m'
bg_roxo    = '\033[45m'
bg_ciano   = '\033[46m'
bg_branco  = '\033[47m'

# ===== Fundo claro =====
bg_preto_c   = '\033[100m'
bg_vermelho_c= '\033[101m'
bg_verde_c   = '\033[102m'
bg_amarelo_c = '\033[103m'
bg_azul_c    = '\033[104m'
bg_roxo_c    = '\033[105m'
bg_ciano_c   = '\033[106m'
bg_branco_c  = '\033[107m'


nomes= []
idades=[]
def procurar_pessoa():
    nome_procura = input(f"{amarelo_c}Digite o nome a procurar:{r} ").strip()

    if nome_procura in nomes:
        indice = nomes.index(nome_procura)
        print(f"{verde}Nome: {nomes[indice]} |{amarelo_c} Idade: {idades[indice]}{r}")
    else:
        print(f"{vermelho}Erro:{vermelho_c}{n} nome não encontrado.{r}")

def adicionar_nome():
    while True:
        try:
            quantidade_nome = int(input(f"{amarelo_c}Quantos nomes quer inserir?{r} "))
            if quantidade_nome <= 0:
                print(f"{vermelho}Insira um número inteiro maior que {branco}{u}zero{r}.")
            else:
                break
        except ValueError:
            print(f"{vermelho}Erro:{n}{vermelho_c} tem de inserir um número inteiro.{r}")

    for i in range(quantidade_nome):
        while True:
            nome = input(f"{ciano_c}Insira o nome {i + 1}:{r} ").strip()

            if not nome.replace(" ", "").isalpha():
                print(f"{vermelho}Erro:{n}{vermelho_c} o nome não pode conter números.{r}")
                continue

            partes = nome.split()
            if not all(p[0].isupper() for p in partes):
                print(f"{vermelho}Erro:{n}{vermelho_c} cada nome deve começar com letra grande.{r}")
                continue

            break

        while True:
            try:
                idade = int(input(f"{azul_c}Insira a idade de {nome}:{r} "))
                break
            except ValueError:
                print(f"{vermelho}Erro:{n}{vermelho_c} a idade tem de ser um número inteiro.{r}")

        nomes.append(nome)
        idades.append(idade)

def mostrar_pessoas():
    if not nomes:
        print(f"{vermelho}{u}Nenhuma pessoa registada.{r}")
        return

    for i in range(len(nomes)):
        print(f"{verde}{i+1}. Nome: {nomes[i]} | Idade: {idades[i]}{r}")

def menu_principal():
    while True:
        print(f"""
{azul_c}{n}╔══════════════════════════════════════╗
║        📋  MENU PRINCIPAL  📋        ║
╠══════════════════════════════════════╣
║ {verde_c}[1]{branco_c} ➜ Adicionar Nome e Idade         ║
║ {ciano_c}[2]{branco_c} ➜ Mostrar Pessoas                ║
║ {amarelo_c}[3]{branco_c} ➜ Procurar Pessoa                ║
║ {vermelho_c}[0]{branco_c} ➜ Sair                           ║
╚══════════════════════════════════════╝{r}
""")

        opcao = input(f"{i}{branco_c}👉 Escolha uma opção: {r}")

        if opcao == "1":
            adicionar_nome()
        elif opcao == "2":
            mostrar_pessoas()
        elif opcao == "3":
            procurar_pessoa()
        elif opcao == "0":
            print(f"{vermelho}{n}A sair... Até breve 👋{r}")
            break
        else:
            print(f"{vermelho}{n}❌ Opção inválida!{r}")


menu_principal()
