# Classe dos Students
class Student:
    name = None
    cpf = None
    weight = 0
    height = 0
    email = None
    imc = None
    status = False

# Classe dos Exercícios
class Exercise:
    exerciseName = None
    numberRepetitions = 0
    exerciseWeight = 0

# Variáveis globais:
registredStudent = []  # lista de Students
exerciseStudent = []  # matriz de treinos

# Recebe os dados para cadastrar o Student.
def cadastreReceive():
    check_if_name_already_exist = 0
    name = input("Insira o nome do novo Aluno: ")
    for i in registredStudent:
        if name == i.name:
            check_if_name_already_exist += 1
    if check_if_name_already_exist == 0:
        cpf = input(f"Insira o CPF de {name}: ")
        if validateCPF(cpf) == True:
            email = input(f"Insira o email de {name}: ")
            if validateEmail(email) == True:
                weight = float(input(f"Insira, em quilogramas, o peso de {name}: "))
                height = int(input(f"Insira a altura de {name}: "))
                imc = calculatingIMC(weight, height)
                studentCadastre(name, cpf, weight, height, email, imc)
                print()
                # print(
                #     f"Nome: {registredStudent[0].name} \nCPF: {registredStudent[0].cpf} \nPeso: {registredStudent[0].weight} kg\nAltura: {registredStudent[0].height} cm\nEmail: {registredStudent[0].email} \nIMC: {registredStudent[0].imc:.2f}\nClassificação do IMC: {registredStudent[0].classingIMC} \n"
                # )
                print(f"Aluno adicionado com sucesso!")
            else:
                print("Email inválido, tente novamente.")
        else:
            print("CPF inválido, tente novamente.")
    else:
        print()
        print(f"O Aluno {name} já existe!")

# Cadastra o Student.
def studentCadastre(name, cpf, weight, height, email, imc):
    new = Student()
    new.name = name
    new.cpf = cpf
    new.weight = weight
    new.height = height
    new.email = email
    new.imc = imc
    new.classingIMC = classifyingIMC(imc)
    new.status = False
    registredStudent.append(new)  # cadastra Student
    exerciseStudent.append([])  # insere um vetor de treinos vazio

# Descobre o Id do Student.
def searchStudentID(name):
    for i in range(len(registredStudent)):
        # print(registredStudent[i].nameExer)
        if name in registredStudent[i].name:
            return i

# Recebe os dados do exercício a ser inserido.
def receiveExercise(idStudent):
    check_if_exercise_already_exist = 0
    nameExer = input("Insira o nome do exercício: ")
    for i in exerciseStudent:
        for j in i:
            if nameExer == j.exerciseName:
                check_if_exercise_already_exist += 1
    if check_if_exercise_already_exist == 0:
        rep = int(input(f"Insira a quantidade de repetições de {nameExer}: "))
        weight = int(input(f"Insira o peso a ser utilizado em {nameExer}: "))
        addExercise(idStudent, nameExer, rep, weight)
    else:
        print("Esse exercício já existe!")

# Insere o exercício.
def addExercise(idStudent, name, rep, weight):
    exer = Exercise()
    exer.exerciseName = name
    exer.numberRepetitions = rep
    exer.exerciseWeight = weight
    registredStudent[idStudent].status = True
    exerciseStudent[idStudent].append(exer)
    # print(exerciseStudent)
    for i in range(len(exerciseStudent[idStudent])):
        print(
            f"\nExercício: {exerciseStudent[idStudent][i].exerciseName} \nNúmero de repetições: {exerciseStudent[idStudent][i].numberRepetitions} \nPeso a ser utilizado: {exerciseStudent[idStudent][i].exerciseWeight}"
        )  # novo exercício no treino do respectivo Student
    print("Exercício adicionado!")

# Altera um exercício existente.
def alterExercise(idStudent, exerciseName):
    check_student_exercise = 0
    for i in exerciseStudent:
        for j in i:
            if j.exerciseName == exerciseName:
                check_student_exercise += 1
    if check_student_exercise > 0:
        for i in exerciseStudent:
            for j in exerciseStudent[idStudent]:
                if j.exerciseName == exerciseName:
                    print(
                        f"Exercício: {j.exerciseName} \nNúmero de repetições: {j.numberRepetitions} \nPeso a ser utilizado: {j.exerciseWeight}"
                    )
                    j.exerciseName = input("Insira o novo nome do exercício: ")
                    j.numberRepetitions = int(
                        input(f"Insira o número de repetições de {j.exerciseName}: ")
                    )
                    j.exerciseWeight = int(
                        input(f"Insira o peso a ser utilizado em {j.exerciseName}: ")
                    )
                    print("Exercício alterado!")
    else:
        print("Exercício não encontrado!")

# Exclui um exercício existente.
def deleteExercise(idStudent, ExerciseExcluir):
    check_exercise_exists = 0
    if len(exerciseStudent[idStudent]) == 0:
        check_exercise_exists += 1
        print("Por favor, primeiro adicione um exercício ao treino!")
    for Exercise in exerciseStudent[idStudent]:
        if ExerciseExcluir == Exercise.exerciseName:
            check_exercise_exists += 1
            print(f"Exercício {Exercise.exerciseName} removido!")
            exerciseStudent[idStudent].remove(Exercise)
            if len(exerciseStudent[idStudent]) == 0:
                registredStudent[idStudent].status = False
    if check_exercise_exists == 0:
        print("Exercício não encontrado!")

# Exclui todos os exercícios do treino de um Student.
def deleteAllExercises(idStudent):
    if len(exerciseStudent[idStudent]) != 0:
        exerciseStudent[idStudent].clear()
        print("Exercícios removidos!")
        registredStudent[idStudent].status = False
    else:
        print("Para remover os exercícios, primeiro adicione eles ao treino!")

# Consulta os dados de um Student.
def viewStudent():
    search_by_name = input("Insinira o nome do aluno que desejas ver os dados: ")
    idStudent = searchStudentID(search_by_name)
    for i in range(len(registredStudent)):
        if search_by_name in registredStudent[i].name:

            print()
            print("Dados do Aluno: ")
            print(f"Nome: {registredStudent[i].name} \nCPF: {registredStudent[i].cpf} \nPeso: {registredStudent[i].weight} kg \nAltura: {registredStudent[i].height} cm\nEmail: {registredStudent[i].email} \nIMC: {registredStudent[i].imc:.2f}\nClassificação do IMC: {registredStudent[i].classingIMC} \n")
            print(" Status:", "Ativo" if registredStudent[i].status == True else "Inativo")
            print()

            if exerciseStudent[i] != []:
                print(f"Treino de {registredStudent[i].name}: ")
                for j in exerciseStudent[idStudent]:
                    print(
                        f"Nome do Exercício: {j.exerciseName}\nNúmero de Repetições: {j.numberRepetitions}\nPeso do Exercício: {j.exerciseWeight} kg\n")
            else:
                print(f"O aluno {search_by_name} ainda não tem um exercício registrado")
        else:
            print(f"O aluno {search_by_name} não está registrado ")

# Atualiza os dados de um Student a partir de seu Id.
def updateData(idStudent):
    print("Se você inserir 0 o elemento previamente cadastrado se manterá!")

    new_name = input(
        f"O nome atualmente cadastrado é: {registredStudent[idStudent].name}. O que você deseja inserir no lugar?\n")
    new_cpf = input(
        f"O CPF atualmente cadastrado é: {registredStudent[idStudent].cpf}. O que você deseja inserir no lugar?\n")
    new_weight = float(input(
        f"O peso atualmente cadastrado é: {registredStudent[idStudent].weight}. O que você deseja inserir no lugar?\n"))
    new_height = int(input(
        f"A altura atualmente cadastrada é: {registredStudent[idStudent].height}. O que você deseja inserir no lugar?\n"))
    new_email = input(
        f"O email atualmente cadastrado é: {registredStudent[idStudent].email}. O que você deseja inserir no lugar?\n")

    if new_name != "0":
        registredStudent[idStudent].name = new_name

    if new_cpf != "0":
        if (validateCPF(new_cpf) == True):
            registredStudent[idStudent].cpf = new_cpf
            if new_email != "0":
                if validateEmail(new_email) == True:
                    registredStudent[idStudent].email = new_email
                    if new_weight != 0:
                        registredStudent[idStudent].weight = new_weight
                        weight_change = True

                    if new_height != 0:
                        registredStudent[idStudent].height = new_height
                        height_change = True
                    
                    if height_change == True or weight_change == True or height_change == True and weight_change == True:
                        registredStudent[idStudent].imc = calculatingIMC(registredStudent[idStudent].weight, registredStudent[idStudent].height)
                
                    print("Dados atualizados com sucesso!!")
                else:
                    print("Email inválido!!")
                    mainMenu()

# Exclui um Student.
def deleteStudent():
    check_student_exists = 0
    name_delete_student = input("Insira o nome do aluno que queres excluir: ")
    for i in registredStudent:
        if name_delete_student == i.name:
            check_student_exists += 1
            print(f"Aluno {i.name} removido!")
            registredStudent.remove(i)
    if check_student_exists == 0:
        print()
        print("Aluno não encontrado!")

# Exibe o relatório de todos os Students.
def reportStudents():
    report_view = input(
        "Escolha que alunos deseja ver: \n1. Todos os alunos\n2. Apenas alunos ativos\n3. Apenas alunos inativos\n"
    )
    match report_view:
        case "1":
            for i in range(len(registredStudent)):
                print()
                print("Dados do Aluno ")
                print(f"Nome: {registredStudent[i].name} \nCPF: {registredStudent[i].cpf}\nPeso: {registredStudent[i].weight} kg\nAltura: {registredStudent[i].height} cm\nEmail: {registredStudent[i].email} \nIMC: {registredStudent[i].imc:.2f}\nClassificação do IMC: {registredStudent[i].classingIMC} \n")
                print(" Status:", "Ativo" if registredStudent[i].status == True else "Inativo")
        case "2":
            for i in range(len(registredStudent)):
                if registredStudent[i].status == True:
                    print()
                    print("Dados do Aluno Ativo: ")
                    print(f"Nome: {registredStudent[i].name} \nCPF: {registredStudent[i].cpf}\nPeso: {registredStudent[i].weight} kg\nAltura: {registredStudent[i].height} cm\nEmail: {registredStudent[i].email} \nIMC: {registredStudent[i].imc:.2f}\nClassificação do IMC: {registredStudent[i].classingIMC} \n")
                else:
                    print("Dentre os Alunos, atualmente nenhum está Ativo")
        case "3":
            for i in range(len(registredStudent)):
                if registredStudent[i].status == False:
                    print()
                    print("Dados do Aluno Inativo: ")
                    print(f"Nome: {registredStudent[i].name} \nCPF: {registredStudent[i].cpf}\nPeso: {registredStudent[i].weight} kg\nAltura: {registredStudent[i].height} cm\nEmail: {registredStudent[i].email} \nIMC: {registredStudent[i].imc:.2f}\nClassificação do IMC: {registredStudent[i].classingIMC} \n")
                else:
                    print("Dentre os Alunos, atualmente nenhum está Inativo")


# Menu principal
def mainMenu():
    openMenu = int(input("Desejais iniciar o Menu?\n1. Sim\n2. Não \n"))
    if openMenu == 1:
        print("Bem vindo ao sistema")
        menu = int(input("Qual operação deseja realizar? \n 1. Cadastrar aluno. \n 2. Gerenciar treino. \n 3. Consultar alunos. \n 4. Atualizar cadastro do aluno. \n 5. Excluir aluno. \n 6. Relatório de aluno. \n 7. Sair \n"))
        if menu == 1:
            print()
            cadastreReceive()
            return True
        if menu == 7:
            return False
        if registredStudent != []:
            if menu == 2:
                print()
                menuManage()
                return True
            elif menu == 3:
                print()
                viewStudent()
                return True
            elif menu == 4:
                print()
                nameStudent = input("Insira o nome do aluno que desejais ver os dados: ")
                idStudent = searchStudentID(nameStudent)
                updateData(idStudent)
                return True
            elif menu == 5:
                print()
                deleteStudent()
                return True
            elif menu == 6:
                print()
                reportStudents()
                return True
            else:
                print("\nPor favor, digite um número válido!")
                return True
        else:
            print("Não há nenhum aluno Cadastrado, por favor, antes de tentar qualquer uma dessas operações, cadastre um aluno!!")
            mainMenu()
    else:
        openMenu = int(input("Desejais iniciar o Menu?\n1. Sim\n2. Não\n"))
        mainMenu()

# Menu Gerenciar Treino
def menuManage():
    student_to_manage_workout = input("Insira o nome do Aluno que deseja gerenciar o treino: ")
    idStudent = searchStudentID(student_to_manage_workout)
    if idStudent != None:
        menuManage = int(
            input(f"Qual operação deseja realizar? \n 1. Incluir um novo exercício no treino de {student_to_manage_workout}. \n 2. Alterar um exercício existente no treino de {student_to_manage_workout}. \n 3. Excluir um exercício do treino de {student_to_manage_workout}. \n 4. Excluir todos os exercícios do treino de {student_to_manage_workout}. \n"))
        if menuManage == 1:
            print()
            receiveExercise(idStudent)

        elif menuManage == 2:
            print()
            Exercisename = input("Insira o nome do exercício que deseja alterar: ")
            print()
            alterExercise(idStudent, Exercisename)

        elif menuManage == 3:
            print()
            ExerciseExcluir = input("Insira o nome do exercício que deseja excluir: ")
            print()
            deleteExercise(idStudent, ExerciseExcluir)
        elif menuManage == 4:
            print()
            confirmation = int(
                input(f"Tem certeza que deseja excluir todos os exercícios de {student_to_manage_workout}? \n1. Sim \n2. Não \n"))
            print()
            if confirmation == 1:
                deleteAllExercises(idStudent)
            elif confirmation == 2:
                print(f"Os exercícios de {student_to_manage_workout} não foram excluídos!")
            else:
                print("Por favor, digite um número válido.")
        else:
            print("Por favor digite um número válido.")
    else:
        print("Aluno não encontrado.")

# def showStudents():
#     if registredStudent == []:
#         print("Não há, atualmente, nenhum aluno cadastrado!!")
        
#     else:
#         print(f"Os alunos atualmente Cadastrados são: {len(registredStudent)}")
#         for i in range(len(registredStudent)):
#             print(f"Aluno {i}: {registredStudent[i].name}")

# def showStudentExercises(idStudent):
    

#                                      Funções para validar CPF e Email, e funções 
#                                           para cálculo e classificação de IMC 
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

def classifyingIMC(imc):
    imc = float(imc)
    if imc < 16.9:
        return "Muito Abaixo do Peso"
    if imc >= 17 and imc <= 18.4:
        return "Abaixo do Peso"
    if imc >= 18.5 and imc <= 24.9:
        return "Normal"
    if imc >= 25 and imc <= 29.9:
        return "Acima do Peso"
    if imc >= 30 and imc <= 34.9:
        return "Obesidade Grau I"
    if imc >= 35 and imc <= 40:
        return "Obesidade Grau II"
    if imc > 40:
        return "Contagem Regressiva"

def calculatingIMC(weight, height):
    if height > 2.2:
        height = height / 100
    IMC = weight / (height * height)
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
        onWorking = mainMenu()
        print()
        if onWorking == True:
            continue
        else:
            break

    except EOFError:
        print("Por favor Andressa, insira alguma coisa.")
        break