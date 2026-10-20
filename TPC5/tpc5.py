##Aplicação para a gestão de alunos

turma = []

opção = -1 

while opção != 0:
    print("MENU DE OPERAÇÕES")
    print("(1) Criar uma turma")
    print("(2) Inserir um aluno na turma")
    print("(3) Listar a turma")
    print("(4) Consultar um aluno por id")
    print("(5) Guardar a turma em ficheiro")
    print("(6) Carregar a turma dum ficheiro")
    print("(0) Sair da aplicação")

    entrada = input("Escolha uma das opções: ")

    if entrada.isdigit():
        opção = int(entrada)

        if opção == 1:
            turma = []
            print("turma criada com sucesso!")

        elif opção == 2:
            nome = input("Introduza o nome do aluno: ")
            Id = input("Introduza o id do aluno: ")
            nota_TPC = float(input("Introduza a nota do TPC (0 a 20): "))
            nota_Projeto = float(input("Introduza a nota do projeto (0 a 20): "))
            nota_Teste = float(input("Introduza a nota do teste (0 a 20): "))

            aluno = (nome, Id, [nota_TPC, nota_Projeto, nota_Teste])
            turma.append(aluno)
            print(f"O aluno {aluno[1]} foi adicionado à turma")

        elif opção == 3:
            if turma == 0:
                print("A turma está vazia. Por favor crie uma turma.")
            else:
                for aluno in turma: 
                    print(f"Nome: {aluno[0]} | Id: {aluno[1]} | Notas: {aluno[2]} ")

        elif opção == 4:
            if turma == 0:
                print("A turma está vazia. Por favor crie uma turma.")
            else:
            
                id_procurado = input("Que id pretende procurar na turma? ")
                posicao_encontrada = -1

                for i in range(len(turma)):
                    if turma[i][1] == id_procurado and posicao_encontrada == -1:
                        posicao_encontrada = i

                if posicao_encontrada != -1:
                    aluno = turma[posicao_encontrada]
                    print(f"Aluno encontrado: Nome: {aluno[0]} | Id: {aluno[1]} | Notas: {aluno[2]}")
                else:
                    print("Aluno não encontrado")

        elif opção == 5:
            if turma == 0:
                print("A turma está vazia. Por favor crie uma turma.")
            else:
                falunos = open("turma.txt","w")

                for aluno in turma:
                    nome = aluno[0]
                    Id = aluno[1]
                    nota_TPC = aluno[2][0]
                    nota_Projeto = aluno[2][1]
                    nota_Teste = aluno[2][2]

                    linha = (f"{nome}; {Id}; {nota_TPC}; {nota_Projeto}; {nota_Teste}\n")
                    falunos.write(linha)

                falunos.close()
                print('A turma foi guardada no ficheiro "turma.txt"!')

        elif opção == 6:
            if turma == 0:
                print("A turma está vazia. Por favor crie uma turma.")
            else:
                falunos = open("turma.txt", "r")
                turma = []

                for linha in falunos:
                    linha = linha.strip()
                    if linha != "":
                        dados = linha.split(";")

                        aluno = (dados[0], dados[1],[float(dados[2]), float(dados[3]), float(dados[4])])
                        turma.append(aluno)

                falunos.close()
                print("A turma foi carregada do ficheiro 'turma.txt' ")

        elif opção == 0:
            print(f"Saindo...Obrigado por usar a aplicação!")

    else:
        print("Resposta Inválida! Por favor selecione uma das opções ")
        opção = -1 
