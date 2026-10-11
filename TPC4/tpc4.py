##Aplicação para manipulação de listas de inteiros

import random

lista_interna = []  #variável interna para guardar a lista de números

opção = -1

while opção != 0:
    print("MENU")
    print("(1) Criar lista")
    print("(2) Ler Lista")
    print("(3) Soma")
    print("(4) Média")
    print("(5) Maior")
    print("(6) Menor")
    print("(7) estaOrdenada por ordem crescente")
    print("(8) estaOrdenada por ordem decrescente")
    print("(9) Procura um elemento")
    print("(0) Sair")

    entrada = input("Escolha uma das opções: ")

    if entrada.isdigit():
        opção = int(entrada)

        if opção == 1:
            tamanho = -1
            lista_interna = []

            while tamanho == -1:
                entrada_tamanho = input("Introduza o número de elementos que quer na lista: ")
                if entrada_tamanho.isdigit():
                    tamanho = int(entrada_tamanho)
                else:
                    print("Resposta Inválida! Por favor selecione o número de elementos que quer na lista: ")

            for elem in range(tamanho):
                numeros_sorteados = random.randint(1,100)
                lista_interna.append(numeros_sorteados)
            print(f"Lista criada com sucesso! {lista_interna}")

        elif opção == 2:
            tamanho = -1 
            lista_interna = []

            while tamanho == -1:
                entrada_tamanho = input("Introduza o número de elementos que quer na lista: ")
                if entrada_tamanho.isdigit():
                    tamanho = int(entrada_tamanho)
                else:
                    print("Resposta Inválida! Por favor selecione o número de elementos que quer na lista: ")

            contador = 0

            while contador < tamanho:
                entrada_numero = input("Introduza um número: ")

                if entrada_numero.isdigit():
                    numero = int(entrada_numero)
                    lista_interna.append(numero)
                    contador = contador + 1
                
                else:
                    print("Resposta Inválida. Por favor introduza um número: ")

            print(f"Lista criada com sucesso!{lista_interna}")

        elif opção == 3:

            if len(lista_interna) == 0:
                print("A lista interna está vazia. Por favor crie uma lista (Opção 1 ou Opção 2)")
            else:
                soma = 0

                for elem in lista_interna:
                    soma = soma + elem
                print(f"A soma dos número da lista é: {soma} ")

        elif opção == 4:

            if len(lista_interna) == 0:
                print("A lista interna está vazia. Por favor crie uma lista (Opção 1 ou Opção 2)")
            else:
                soma = 0 

            for elem in lista_interna:
                soma = soma + elem
                média = soma / tamanho
            print(f"A média da lista é: {média}")

        elif opção == 5:
            if lista_interna == 0:
                print("A lista interna está vazia. Por favor cire uma lista (Opção 1 ou Opção 2)")
            else:
                maior = lista_interna[0]

                for elem in lista_interna:
                    if elem > maior:
                        maior = elem
                        
                print(f"O maior elemento da lista é {maior}")

        elif opção == 6:
            if lista_interna == 0:
                print("A lista interna está vazia. Por favor cire uma lista (Opção 1 ou Opção 2)")
            else:
                menor = lista_interna[0]

                for elem in lista_interna:
                    if elem < menor:
                        menor = elem
                print(f"O menor elemento da lista é {menor}")

        elif opção == 7:
            if lista_interna == 0:
                print("A lista interna está vazia. Por favor cire uma lista (Opção 1 ou Opção 2)")
            else:
                ordenada = True
                for i in range(len(lista_interna)-1):
                    if lista_interna[i] > lista_interna[i + 1]:
                        ordenada = False
                if ordenada:
                    print("Sim")
                else:
                    print("Não")

        elif opção == 8:
            if lista_interna == 0:
                print("A lista interna está vazia. Por favor cire uma lista (Opção 1 ou Opção 2)")
            else:
                ordenada = True
                for i in range(len(lista_interna)-1):
                    if lista_interna[i] < lista_interna[i + 1]:
                        ordenada = False
                if ordenada:
                    print("Sim")
                else:
                    print("Não")

        elif opção == 9:
            if lista_interna == 0:
                print("A lista interna está vazia. Por favor crie uma lista (Opção 1 ou Opção 2)")
            else:
                entrada_procura  = input("Que número quer procurar na lista? ")

                if entrada_procura.isdigit():
                    numero_procurado = int(entrada_procura)
                    posição_encontrada = -1

                    for i in range(len(lista_interna)):
                        if lista_interna[i] == numero_procurado and posição_encontrada == -1:
                            posição_encontrada = i

                    if posição_encontrada != -1:
                        print(f"O elemento foi encontrado na posição: {posição_encontrada}")
                    else:
                        print(f"O elemento não está na lista. Resultado: {posição_encontrada}")
                            

                else:
                     print("Resposta Inválida! Por favor escolha um número para ser procurado na lista: ")

        elif opção == 0:
            print(f"Obrigado por usar a aplicação!! A lista final guardada foi: {lista_interna}")
                    
    else:
        print("Resposta inválida! Por favor selecione uma das opções!")
        opção = -1


