#Corrida para o 100

jogar_novamente = "s"

while jogar_novamente == "s" or jogar_novamente == "S":

    print("CORRIDA PARA O 100")
    print("1 - O utilizador joga primeiro.")
    print("2 - O computador joga primeiro.")

    vertente = input("Selecione uma das vertentes:")

    while vertente != "1" and vertente != "2":
        print("Resposta inválida")
        print("CORRIDA PARA O 100")
        print("1 - O utilizador joga primeiro.")
        print("2 - O computador joga primeiro.")
        
        vertente = input("Por favor selecione qual vertente pretende jogar:")

    soma = 0

    if vertente == "1":
        while soma < 100:
            jogada = input(f"Selecione um número entre 1 e 10:")
            if jogada.isdigit():
                jogada_user = int(jogada)

                if 1 <= jogada_user <= 10:
                    soma = soma + jogada_user
                    print(f"Selecionou {jogada_user}. A soma atual é de {soma}.")
                    
                    if soma >= 100:
                        print("Parabéns! Venceu o jogo!")
                    else:
                        resto = soma % 11
                        if resto == 1 or resto == 0:
                            jogada_cpu = 1
                        else:
                            jogada_cpu = 11 - resto
                            soma = soma + jogada_cpu
                            print(f"O computador selecionou {jogada_cpu}. A soma atual é de {soma}.")

                            if soma >= 100:
                                print("O computador venceu!")
                else:
                    print("Número Inválido.")
                    print("Por favor selecione um número entre 1 e 10:")

            else:
                print("Resposta Inválida")
                print("Por favor, selecione um número entre 1 e 10:")

    elif vertente == "2":
            jogada_cpu = 1
            soma = soma + jogada_cpu
            print(f"O computador selecionou {jogada_cpu}. A soma atual é de {soma}.")

            while soma < 100:
                jogada = input(f"Selecione um número entre 1 e 10:")

                if jogada.isdigit():
                    jogada_user = int(jogada)

                    if 1<= jogada_user <= 10:
                        soma = soma + jogada_user
                        print(f"Selecionou {jogada_user}. A soma atual é de {soma}")

                        if soma >= 100:
                            print("Parabéns! Venceu o jogo!")
                        else:
                            jogada_cpu = 11 - jogada_user
                            soma = soma + jogada_cpu
                            print(f"O computador selecionou {jogada_cpu}. A soma atual é de {soma}.")

                            if soma >= 100:
                                print("O computador venceu!")

                    else:
                        print("Número Inválido")
                        print("Por favor selecione um número entre 1 e 10:")
                        
                else:
                    print("Resposta Inválida")
                    print("Por favor selecione um número entre 1 e 10:")

    jogar_novamente = input("Pretende jogar novamente?")

print("Obrigado por jogar!")



