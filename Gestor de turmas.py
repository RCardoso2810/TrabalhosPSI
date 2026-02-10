# ================= CORES (ANSI) =================
RESET = "\033[0m"
VERDE = "\033[92m"
VERMELHO = "\033[91m"
AZUL = "\033[94m"
AMARELO = "\033[93m"
CIANO = "\033[96m"

# Estrutura principal da escola
escola = {
    "nome": "",
    "cursos": {},
    "alunos_sem_curso": []
}

# ================= UTILIDADES =================

def limpar_tela():
    """Limpa o ecrã imprimindo várias linhas."""
    print("\n" * 50)

def validar_nome(texto):
    """Valida um nome: apenas letras e com inicial maiúscula."""
    return texto.isalpha() and texto.istitle()

def validar_nome_escola(nome):
    """Valida o nome da escola: só letras, pode ter espaços, e cada palavra começa com maiúscula."""
    nome = nome.strip()
    if not nome:
        return False
    palavras = nome.split()
    return all(palavra.isalpha() and palavra[0].isupper() for palavra in palavras)

def validar_idade(idade):
    """Valida idade entre 0 e 100."""
    return 0 <= idade <= 100

def validar_nome_curso(nome):
    """Valida nome do curso: só letras, pode ter espaços, começa por maiúscula."""
    nome = nome.strip()
    if not nome:
        return False
    palavras = nome.split()
    return all(p.isalpha() for p in palavras) and nome[0].isupper()

def pedir_numero(msg):
    """Pede um número inteiro maior que 0."""
    while True:
        try:
            n = int(input(msg))
            if n > 0:
                return n
            else:
                print("O número tem de ser maior que 0")
        except ValueError:
            print("Não é permitido letras, apenas números")

def organizar_turnos(turnos):
    """
    Organiza os turnos de uma turma alternando alunos por ordem alfabética.
    Exemplo: turno 1 e turno 2 ficam equilibrados.
    """
    todos = turnos[0] + turnos[1]
    todos.sort(key=lambda x: (x["sobrenome"], x["nome"]))
    turnos[0].clear()
    turnos[1].clear()

    for i, aluno in enumerate(todos):
        turnos[i % 2].append(aluno)

# ================= CONFIGURAÇÃO =================

def configurar_escola():
    """Configura o nome da escola e cria os cursos iniciais."""
    while True:
        nome = input("Nome da escola: ")
        if validar_nome_escola(nome):
            escola["nome"] = nome
            break
        else:
            print("O nome da escola tem de começar com letra maiúscula e não pode conter números")

    n = pedir_numero("Quantos cursos? ")

    for _ in range(n):
        while True:
            curso = input("Nome do curso: ").strip()
            if validar_nome_curso(curso):
                if curso not in escola["cursos"]:
                    break
                else:
                    print("Curso já existe")
            else:
                print("Nome inválido (só letras, pode ter espaços, começa por maiúscula)")

        escola["cursos"][curso] = {
            "turmas": {},
            "materias": {}
        }

        qtd = pedir_numero("Quantas turmas por ano? ")
        letras = [chr(65 + i) for i in range(qtd)]

        for ano in ["10º", "11º", "12º"]:
            for l in letras:
                escola["cursos"][curso]["turmas"][f"{ano}{l}"] = {
                    "alunos": [[], []]
                }

# ================= CURSOS =================

def adicionar_curso():
    """Adiciona um novo curso."""
    while True:
        curso = input("Nome do curso: ").strip()
        if validar_nome_curso(curso):
            if curso in escola["cursos"]:
                print("Curso já existe")
            else:
                escola["cursos"][curso] = {"turmas": {}, "materias": {}}
                print("Curso adicionado com sucesso")
                return
        else:
            print("Nome inválido (só letras, pode ter espaços, começa por maiúscula)")

def remover_curso():
    """Remove um curso e envia todos os alunos para 'alunos sem curso'."""
    curso = escolher_curso()
    if not curso:
        return

    # Percorrer todas as turmas do curso
    for turma in escola["cursos"][curso]["turmas"].values():
        for turno in turma["alunos"]:
            for aluno in turno:
                escola["alunos_sem_curso"].append(aluno)

    # Agora sim, remover o curso
    del escola["cursos"][curso]

    print("Curso removido. Todos os alunos ficaram sem curso.")

# ================= SELEÇÕES =================

def escolher_curso():
    """Mostra os cursos disponíveis e permite escolher um por nome."""
    if not escola["cursos"]:
        print("Não existem cursos")
        return None

    for c in escola["cursos"]:
        print("-", c)

    curso = input("Curso: ").strip()
    if curso not in escola["cursos"]:
        print("Curso inválido")
        return None

    return curso

def escolher_turma(curso):
    """
    Escolhe uma turma por número (1,2,3...).
    Isto evita ter de escrever o nome completo da turma.
    """
    turmas = escola["cursos"][curso]["turmas"]
    if not turmas:
        print("Este curso não tem turmas")
        return None

    lista = list(turmas.keys())
    for i, t in enumerate(lista, start=1):
        print(f"{i} - {t}")

    while True:
        try:
            opcao = int(input("Escolha a turma (número): "))
            if 1 <= opcao <= len(lista):
                return turmas[lista[opcao - 1]]
            else:
                print("Número inválido")
        except ValueError:
            print("Só números")

# ================= ALUNOS =================

def adicionar_aluno():
    """Adiciona um aluno a uma turma escolhida."""
    curso = escolher_curso()
    if not curso:
        return

    turma = escolher_turma(curso)
    if not turma:
        print("Não foi possível escolher turma.")
        return

    while True:
        nome = input("Nome: ").strip()
        if validar_nome(nome):
            break
        print("Nome inválido")

    while True:
        sobrenome = input("Sobrenome: ").strip()
        if validar_nome(sobrenome):
            break
        print("Sobrenome inválido")

    while True:
        try:
            idade = int(input("Idade: "))
            if validar_idade(idade):
                break
            print("Idade tem de ser entre 0 e 100")
        except ValueError:
            print("Só números")

    aluno = {
        "nome": nome,
        "sobrenome": sobrenome,
        "idade": idade
    }

    turma["alunos"][0].append(aluno)
    organizar_turnos(turma["alunos"])
    print("Aluno adicionado com sucesso")

def remover_aluno():
    """Remove um aluno de qualquer turma ou da lista sem curso."""
    nome = input("Nome do aluno: ").strip()
    sobrenome = input("Sobrenome do aluno: ").strip()

    for curso in escola["cursos"].values():
        for turma in curso["turmas"].values():
            for turno in turma["alunos"]:
                for aluno in turno[:]:
                    if aluno["nome"] == nome and aluno["sobrenome"] == sobrenome:
                        turno.remove(aluno)
                        organizar_turnos(turma["alunos"])
                        print("Aluno removido")
                        return

    for aluno in escola["alunos_sem_curso"][:]:
        if aluno["nome"] == nome and aluno["sobrenome"] == sobrenome:
            escola["alunos_sem_curso"].remove(aluno)
            print("Aluno removido (sem curso)")
            return

    print("Aluno não encontrado")

# ================= MATÉRIAS / PROFESSORES =================

def adicionar_materia():
    """Adiciona uma matéria a um curso."""
    curso = escolher_curso()
    if not curso:
        return

    materia = input("Nome da matéria: ").strip()
    escola["cursos"][curso]["materias"][materia] = []
    print("Matéria adicionada com sucesso")

def adicionar_professor():
    """Adiciona um professor a uma matéria específica."""
    curso = escolher_curso()
    if not curso:
        return

    for m in escola["cursos"][curso]["materias"]:
        print("-", m)

    m = input("Matéria: ").strip()
    if m not in escola["cursos"][curso]["materias"]:
        print("Matéria inválida")
        return

    prof = input("Nome do professor: ").strip()
    escola["cursos"][curso]["materias"][m].append(prof)
    print("Professor adicionado com sucesso")

def remover_professor():
    """Remove um professor de uma matéria."""
    curso = escolher_curso()
    if not curso:
        return

    materia = input("Matéria: ").strip()
    prof = input("Professor: ").strip()

    try:
        escola["cursos"][curso]["materias"][materia].remove(prof)
        print("Professor removido")
    except (KeyError, ValueError):
        print("Erro ao remover professor")

# ================= MOSTRAR =================

def mostrar_turmas():
    """Mostra todas as turmas e alunos por curso."""
    if not escola["cursos"]:
        print("Não existem cursos")
        return

    for curso, dados in escola["cursos"].items():
        sigla = curso.upper()
        print(f"\nCurso: {sigla}")

        if not dados["turmas"]:
            print("  Este curso não tem turmas")
            continue

        tem_alunos = False

        for t, info in dados["turmas"].items():
            print(f" {t}")

            for i, turno in enumerate(info["alunos"], start=1):
                print(f"  Turno {i}:")

                if turno:
                    tem_alunos = True
                    for a in turno:
                        print(f"   {a['nome']} {a['sobrenome']}")
                else:
                    print("   (Sem alunos)")

        if not tem_alunos:
            print("  Este curso não tem alunos")

def mostrar_alunos_sem_curso():
    """Mostra alunos que ainda não têm curso."""
    if not escola["alunos_sem_curso"]:
        print("Não existem alunos sem curso")
        return

    print("\nAlunos sem curso:")
    for a in escola["alunos_sem_curso"]:
        print(f"- {a['nome']} {a['sobrenome']} ({a['idade']} anos)")

# ================= ESTATÍSTICAS =================

def estatisticas():
    """Mostra estatísticas da escola (total de alunos e idade média)."""
    total = 0
    soma = 0

    for curso in escola["cursos"].values():
        for turma in curso["turmas"].values():
            for turno in turma["alunos"]:
                for a in turno:
                    total += 1
                    soma += a["idade"]

    for a in escola["alunos_sem_curso"]:
        total += 1
        soma += a["idade"]

    print("Total de alunos:", total)
    if total:
        print("Idade média:", soma / total)

# ================= MENU =================

def menu():
    """Menu principal com todas as opções."""
    while True:
        limpar_tela()

        print(CIANO + f"""
 {escola["nome"]}
 -----------------------
 1 - Adicionar aluno
 2 - Remover aluno
 3 - Adicionar matéria
 4 - Adicionar professor
 5 - Remover professor
 6 - Mostrar turmas
 7 - Estatísticas
 8 - Adicionar curso
 9 - Remover curso
 10 - Mostrar alunos sem curso
 0 - Sair
 """ + RESET)

        op = input("Opção: ")

        if op == "1":
            adicionar_aluno()
        elif op == "2":
            remover_aluno()
        elif op == "3":
            adicionar_materia()
        elif op == "4":
            adicionar_professor()
        elif op == "5":
            remover_professor()
        elif op == "6":
            mostrar_turmas()
        elif op == "7":
            estatisticas()
        elif op == "8":
            adicionar_curso()
        elif op == "9":
            remover_curso()
        elif op == "10":
            mostrar_alunos_sem_curso()
        elif op == "0":
            break
        else:
            print("Opção inválida")

        input("\nEnter para continuar...")

# ================= INÍCIO =================

configurar_escola()
menu()
