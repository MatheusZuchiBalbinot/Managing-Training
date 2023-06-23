# Classe dos Alunos
class Aluno:
    nome = None
    cpf = None
    peso = 0
    altura = 0
    email = None
    imc = None
    status = False

# Classe dos Exercícios
class Exercicio:
    nomeExercicio = None
    numRepeticoes = 0
    pesoExercicio = 0

# Variáveis globais:
cadAlunos = []  # lista de alunos
treinoAlunos = []  # matriz de treinos

# Recebe os dados para cadastrar o aluno.
def recebeCadastro():
    verificacao = 0
    nome = input("Insira o nome do novo aluno: ")
    for i in cadAlunos:
        if nome == i.nome:
            verificacao += 1
    if verificacao == 0:
        cpf = input(f"Insira o cpf de {nome}: ")
        if validateCPF(cpf) == True:
            email = input(f"Insira o email de {nome}: ")
            if validateEmail(email) == True:
                peso = float(input(f"Insira, em quilogramas, o peso de {nome}: "))
                altura = int(input(f"Insira a altura de {nome}: "))
                imc = calculatingIMC(peso, altura)
                cadastroAluno(nome, cpf, peso, altura, email, imc)
                print()
                print(
                    f"Nome: {cadAlunos[0].nome} \nCPF: {cadAlunos[0].cpf} \nPeso: {cadAlunos[0].peso} kg \nAltura: {cadAlunos[0].altura} cm\nEmail: {cadAlunos[0].email} \nIMC: {cadAlunos[0].imc:.2f}"
                )
                print(f"Aluno adicionado com sucesso!")
            else:
                print("Email inválido, tente novamente.")
        else:
            print("CPF inválido, tente novamente.")
    else:
        print()
        print(f"O aluno {nome} já existe!")

# Cadastra o aluno.
def cadastroAluno(nome, cpf, peso, altura, email, imc):
    novo = Aluno()
    novo.nome = nome
    novo.cpf = cpf
    novo.peso = peso
    novo.altura = altura
    novo.email = email
    novo.imc = imc
    novo.status = False
    cadAlunos.append(novo)  # cadastra aluno
    treinoAlunos.append([])  # insere um vetor de treinos vazio

# Descobre o Id do Aluno.
def descobreIdAluno(nome):
    for i in range(len(cadAlunos)):
        # print(cadAlunos[i].nomeExer)
        if nome in cadAlunos[i].nome:
            return i

# Recebe os dados do exercício a ser inserido.
def recebeExercicio(idAluno):
    verificando = 0
    nomeExer = input("Insira o nome do exercício: ")
    for i in treinoAlunos:
        for j in i:
            if nomeExer == j.nomeExercicio:
                verificando += 1
    if verificando == 0:
        rep = int(input(f"Insira a quantidade de repetições de {nomeExer}: "))
        peso = int(input(f"Insira o peso a ser utilizado em {nomeExer}: "))
        insereExercicio(idAluno, nomeExer, rep, peso)
    else:
        print("Esse exercício já existe!")

# Insere o exercício.
def insereExercicio(idAluno, nome, rep, peso):
    exer = Exercicio()
    exer.nomeExercicio = nome
    exer.numRepeticoes = rep
    exer.pesoExercicio = peso
    cadAlunos[idAluno].status = True
    treinoAlunos[idAluno].append(exer)
    # print(treinoAlunos)
    for i in range(len(treinoAlunos[idAluno])):
        print(
            f"Exercício: {treinoAlunos[idAluno][i].nomeExercicio} \nNúmero de repetições: {treinoAlunos[idAluno][i].numRepeticoes} \nPeso a ser utilizado: {treinoAlunos[idAluno][i].pesoExercicio}"
        )  # novo exercício no treino do respectivo aluno
    print("Exercício adicionado!")

# Altera um exercício existente.
def alteraExercicio(idAluno, nomeExercicio):
    verificador = 0
    for i in treinoAlunos:
        for j in i:
            if j.nomeExercicio == nomeExercicio:
                verificador += 1
    if verificador > 0:
        for i in treinoAlunos:
            for j in treinoAlunos[idAluno]:
                if j.nomeExercicio == nomeExercicio:
                    print(
                        f"Exercício: {j.nomeExercicio} \nNúmero de repetições: {j.numRepeticoes} \nPeso a ser utilizado: {j.pesoExercicio}"
                    )
                    j.nomeExercicio = input("Insira o novo nome do exercício: ")
                    j.numRepeticoes = int(
                        input(f"Insira o número de repetições de {j.nomeExercicio}: ")
                    )
                    j.pesoExercicio = int(
                        input(f"Insira o peso a ser utilizado em {j.nomeExercicio}: ")
                    )
                    print("Exercício alterado!")
    else:
        print("Exercício não encontrado!")

# Exclui um exercício existente.
def excluirExercicio(idAluno, exercicioExcluir):
    verificador = 0
    if len(treinoAlunos[idAluno]) == 0:
        verificador += 1
        print("Por favor, primeiro adicione um exercício ao treino!")
    for exercicio in treinoAlunos[idAluno]:
        if exercicioExcluir == exercicio.nomeExercicio:
            verificador += 1
            print(f"Exercício {exercicio.nomeExercicio} removido!")
            treinoAlunos[idAluno].remove(exercicio)
            if len(treinoAlunos[idAluno]) == 0:
                cadAlunos[idAluno].status = False
    if verificador == 0:
        print("Exercício não encontrado!")

# Exclui todos os exercícios do treino de um aluno.
def excluirTodosExercicios(idAluno):
    if len(treinoAlunos[idAluno]) != 0:
        treinoAlunos[idAluno].clear()
        print("Exercícios removidos!")
        cadAlunos[idAluno].status = False
    else:
        print("Para remover os exercícios, primeiro adicione eles ao treino!")

# Consulta os dados de um aluno.
def consultarAluno():
    search_by_name = input("Input the name of the pupil you want to view the data: ")
    idAluno = descobreIdAluno(search_by_name)
    for i in range(len(cadAlunos)):
        if search_by_name in cadAlunos[i].nome:
            if treinoAlunos[i] != []:
                print()
                print("Pupil Data: ")
                print(f" Nome: {cadAlunos[0].nome} \nCPF: {cadAlunos[0].cpf} \nPeso: {cadAlunos[0].peso} kg \nAltura: {cadAlunos[0].altura} cm\nEmail: {cadAlunos[0].email} \nIMC: {cadAlunos[0].imc:.2f}")
                print(" Status:", "Ativo" if cadAlunos[i].status == True else "Inativo")
                print()
                print(f"Treino de {cadAlunos[i].nome}: ")
                for j in treinoAlunos[idAluno]:
                    print(
                        f" Nome do Exercício: {j.nomeExercicio}\n Número de Repetições: {j.numRepeticoes}\n Peso do Exercício: {j.pesoExercicio} kg")
            else:
                print(f"The Pupil {search_by_name} does't have a registred workout")
        else:
            print(f"The Pupil {search_by_name} is not registred ")

# Atualiza os dados de um aluno a partir de seu Id.
def atualizarDados(idAluno):
    print("if you enter 0 will stay the same!")

    new_name = input(
        f"The actual Name is: {cadAlunos[idAluno].nome}. What do you want to put?\n")
    new_cpf = input(
        f"The actual CPF is: {cadAlunos[idAluno].cpf}. What do you want to put?\n")
    new_weight = input(
        f"The actual Weight is: {cadAlunos[idAluno].peso}. What do you want to put?\n")
    new_height = input(
        f"The actual Height is: {cadAlunos[idAluno].altura}. What do you want to put?\n")
    new_email = input(
        f"The actual Email is: {cadAlunos[idAluno].email}. What do you want to put?\n")

    if new_name != "0":
        cadAlunos[idAluno].nome = new_name

    if new_cpf != "0":
        if (validateCPF(new_cpf) == True):
            cadAlunos[idAluno].cpf = new_cpf
        else:
            print("CPF inválido!!")

    if new_weight != "0":
        cadAlunos[idAluno].peso = new_weight
        weight_change = True

    if new_height != "0":
        cadAlunos[idAluno].altura = new_height
        height_change = True
    
    if height_change == True or weight_change == True or height_change == True and weight_change == True:
        cadAlunos[idAluno].imc = calculatingIMC(cadAlunos[idAluno].peso, cadAlunos[idAluno].altura)

    if new_email != "0":
        if validateEmail(new_email) == True:
            cadAlunos[idAluno].email = new_email
        else:
            print("Email inválido!!")

# Exclui um aluno.
def excluirAluno():
    verificador = 0
    name_delete_pupil = input("Input the name of the pupil you want to delete data: ")
    for i in cadAlunos:
        if name_delete_pupil == i.nome:
            verificador += 1
            print(f"Aluno {i.nome} removido!")
            cadAlunos.remove(i)
    if verificador == 0:
        print()
        print("Aluno não encontrado!")

# Exibe o relatório de todos os alunos.
def relatorioAlunos():
    report_view = input(
        "Choose what you want to view: \n 1. All Pupils \n 2. Just Active Pupils\n 3. Just Inactive Pupils\n"
    )
    match report_view:
        case "1":
            for i in range(len(cadAlunos)):
                print()
                print("Pupil Data: ")
                print(f" Nome: {cadAlunos[0].nome} \nCPF: {cadAlunos[0].cpf} \nPeso: {cadAlunos[0].peso} kg \nAltura: {cadAlunos[0].altura} cm\nEmail: {cadAlunos[0].email} \nIMC: {cadAlunos[0].imc:.2f}")
                print(" Status:", "Ativo" if cadAlunos[i].status == True else "Inativo")
        case "2":
            for i in range(len(cadAlunos)):
                if cadAlunos[i].status == True:
                    print()
                    print("Active Pupil Data: ")
                    print(f" Nome: {cadAlunos[0].nome} \nCPF: {cadAlunos[0].cpf} \nPeso: {cadAlunos[0].peso} kg \nAltura: {cadAlunos[0].altura} cm\nEmail: {cadAlunos[0].email} \nIMC: {cadAlunos[0].imc:.2f}")
        case "3":
            for i in range(len(cadAlunos)):
                if cadAlunos[i].status == False:
                    print()
                    print("Inative Pupil Data: ")
                    print(f" Nome: {cadAlunos[0].nome} \nCPF: {cadAlunos[0].cpf} \nPeso: {cadAlunos[0].peso} kg \nAltura: {cadAlunos[0].altura} cm\nEmail: {cadAlunos[0].email} \nIMC: {cadAlunos[0].imc:.2f}")

# Verifica se o cpf é válido.
def validateCPF(cpf):

    sum_of_multiplication = []
    result_of_multiplication = []
    verifications_digits = []
    rearranging_cpf = list(cpf)

    for j in rearranging_cpf:
        if j == '.' or j == '-':
            rearranging_cpf.remove(j)
    realCPF = rearranging_cpf
    rearranging_cpf = list(map(int, rearranging_cpf))

    rearranging_cpf.pop(-1)
    rearranging_cpf.pop(-1)
    elements_to_multiplicate = range(10,1,-1) 

    def multiplePerDigit(rearranging_cpf, elements_to_multiplicate):
        for i in range(len(rearranging_cpf)):
            result = rearranging_cpf[i] * elements_to_multiplicate[i]
            result_of_multiplication.append(result)

    multiplePerDigit(rearranging_cpf, elements_to_multiplicate)
    sum_of_multiplication = sum(result_of_multiplication)

    def calculateVerificationDigits(sum):
        leftover = sum % 11

        if leftover == 0 or leftover == 1 or leftover > 10:
            return verifications_digits.append(0)
        else:
            first_digit = 11 - leftover
            return verifications_digits.append(first_digit)

    calculateVerificationDigits(sum_of_multiplication)
    elements_to_multiplicate = [*range(11,1,-1)]
    rearranging_cpf.append(verifications_digits[0])
    result_of_multiplication.clear()

    multiplePerDigit(rearranging_cpf, elements_to_multiplicate)
    sum_of_multiplication = sum(result_of_multiplication)

    calculateVerificationDigits(sum_of_multiplication)
    rearranging_cpf.append(verifications_digits[1])

    def finalCheck(realCPF, rearranging_cpf):
        realCPF = list(map(int, realCPF))
        if realCPF == rearranging_cpf:
            return True
        else:
            return False

    return finalCheck(realCPF, rearranging_cpf)

# Menu principal
def menuPrincipal():
    print("Bem vindo ao sistema")
    menu = int(input("Qual operação deseja realizar? \n 1. Cadastrar aluno. \n 2. Gerenciar treino. \n 3. Consultar aluno. \n 4. Atualizar cadastro do aluno. \n 5. Excluir aluno. \n 6. Relatório de alunos. \n 7. Sair \n"))
    if menu == 1:
        print()
        recebeCadastro()
        return True
    elif menu == 2:
        print()
        menuGerenciar()
        return True
    elif menu == 3:
        print()
        consultarAluno()
        return True
    elif menu == 4:
        print()
        nomeAluno = input("Input the name of the pupil you want to view the data: ")
        idAluno = descobreIdAluno(nomeAluno)
        atualizarDados(idAluno)
        return True
    elif menu == 5:
        print()
        excluirAluno()
        return True
    elif menu == 6:
        print()
        relatorioAlunos()
        return True
    elif menu == 7:
        return False
    else:
        print("\nPor favor, digite um número válido!")
        return True

# Menu Gerenciar Treino
def menuGerenciar():
    aluno1 = input("Insira o nome do aluno que deseja gerenciar o treino: ")
    idAluno = descobreIdAluno(aluno1)
    if idAluno != None:
        menuGerenciar = int(
            input(f"Qual operação deseja realizar? \n 1. Incluir um novo exercício no treino de {aluno1}. \n 2. Alterar um exercício existente no treino de {aluno1}. \n 3. Excluir um exercício do treino de {aluno1}. \n 4. Excluir todos os exercícios do treino de {aluno1}. \n"))
        if menuGerenciar == 1:
            print()
            recebeExercicio(idAluno)

        elif menuGerenciar == 2:
            print()
            exercicioNome = input("Insira o nome do exercício que deseja alterar: ")
            print()
            alteraExercicio(idAluno, exercicioNome)

        elif menuGerenciar == 3:
            print()
            exercicioExcluir = input("Insira o nome do exercício que deseja excluir: ")
            print()
            excluirExercicio(idAluno, exercicioExcluir)
        elif menuGerenciar == 4:
            print()
            certeza = int(
                input(f"Tem certeza que deseja excluir todos os exercícios de {aluno1}? \n1. Sim \n2. Não \n"))
            print()
            if certeza == 1:
                excluirTodosExercicios(idAluno)
            elif certeza == 2:
                print(f"Os exercícios de {aluno1} não foram excluídos!")
            else:
                print("Por favor, digite um número válido.")
        else:
            print("Por favor digite um número válido.")
    else:
        print("Aluno não encontrado.")

def calculatingIMC(peso, altura):
    if altura > 2.2:
        altura = altura / 100
    IMC = peso / (altura * altura)
    rounded_imc = round(IMC)
    return rounded_imc

import re

def validateEmail(email):
    r = re.compile(r"^[\w-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$")
    if r.match(email):
        return True
    else:
        return False

# main
while True:
    try:
        confirmacao = menuPrincipal()
        print()
        if confirmacao == True:
            continue
        else:
            break

    except EOFError:
        print("Por favor Andressa, insira alguma coisa.")
        break