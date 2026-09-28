# Adivinha o número
import random

print("Jogo: Adivinha o número")
print("1 - O utilizador adivinha o número do computador. ")
print("2 - O computador adivinha o número do utilizador. ")

modo = input("Ecolha um dos dois modos: ")

while modo != "1" and modo != "2":
    print("Resposta Inválida")
    print("Jogo: Adivinha o Número")
    print("1 - O utilizador adivinha o número do computador.")
    print("2 - O computador adivinha o número do utilizador.")

    modo = input("Escolha o modo 1 ou 2: ")

if modo == "1":

    minimo = 0
    maximo = 100
    resposta = random.randint(minimo, maximo)
    tentativas = 0
    palpite = 0


    print("Adivinha o número")
    print(f"Seleciona um número entre {minimo} e {maximo}: ")

    while palpite != resposta:

        palpite = input("Dá o teu palpite: ")
        if palpite.isdigit():
            palpite =  int(palpite)
            tentativas = tentativas + 1

            if palpite > maximo or palpite < minimo:
                print("Palpite inválido.")
                print(f"Por favor selecione um número entre {minimo} e {maximo}: ")
            elif palpite < resposta:
                print("O número que pensei é Maior")
            elif palpite > resposta:
                print("O número que pensei é Menor")
            else:
                print("Acertou")
                print(f"O número de tentativas foi: {tentativas}")

        else:
            print("Palpite inválido")
            print(f"Por favor selecione um número entre {minimo} e {maximo}: ")


else:

    minimo = 0
    maximo = 100
    resposta = ""
    tentativas = 0

    print(f"Pensa num número entre {minimo} e {maximo} ")
    print("Responde aos meus palpites com uma das seguintes instruções: ")
    print("-Acertou")
    print("-Maior")
    print("-Menor")

    while resposta != "Acertou": 
        palpite = (maximo + minimo) // 2
        tentativas = tentativas + 1
        print(f"O meu palpite é {palpite}")
        resposta = input("Qual é a tua resposta?")

        if resposta == "Maior":
            minimo = palpite + 1
        elif resposta == "Menor":
            maximo = palpite - 1
        elif resposta == "Acertou":
            print(f"Acertei! O número que pensaste é {palpite}")
            print(f"O número de tentativas foi: {tentativas}")
        else:
            print("Resposta inválida.")
            print("Por favor escreva um das 3 instruções referidas acima.")

