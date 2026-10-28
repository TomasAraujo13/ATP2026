# TPC6 — Aplicação de meteorologia
# Modelo: TabMeteo = [(Data, TempMin, TempMax, Precipitacao)]
# Data = (Ano, Mes, Dia)

from matplotlib import pyplot as plt

def menu():
    print("""
MENU METEOROLÓGICO
1: Calcular a temperatura média de cada dia
2: Guardar a tabela meteorológica num ficheiro
3: Carregar uma tabela meteorológica de um ficheiro
4: Calcular a temperatura mínima mais baixa
5: Calcular a amplitude térmica de cada dia
6: Encontrar o dia com precipitação máxima
7: Listar dias com precipitação superior a um limite
8: Calcular o maior período consecutivo com precipitação abaixo de um limite
9: Desenhar gráficos da temperatura mínima, máxima e pluviosidade
0: Sair da aplicação
""")


def dataTexto(data):
    ano, mes, dia = data
    return f"{ano}-{mes}-{dia}"


def medias(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        res.append((data, (tmin + tmax) / 2))
    return res


def guardaTabMeteo(tabMeteo, fnome):
    with open(fnome, "w") as ficheiro:
        for data, tmin, tmax, prec in tabMeteo:
            ficheiro.write(f"{dataTexto(data)}|{tmin}|{tmax}|{prec}\n")


def carregaTabMeteo(fnome):
    res = []
    with open(fnome, "r") as ficheiro:
        for linha in ficheiro:
            linha = linha.strip()
            if linha != "":
                partes = linha.split("|")
                dataTextoFicheiro = partes[0]
                ano, mes, dia = dataTextoFicheiro.split("-")
                data = (int(ano), int(mes), int(dia))
                tmin = float(partes[1])
                tmax = float(partes[2])
                prec = float(partes[3])
                res.append((data, tmin, tmax, prec))
    return res


def minMin(tabMeteo):
    if len(tabMeteo) == 0:
        return None
    minima = tabMeteo[0][1]
    for data, tmin, tmax, prec in tabMeteo:
        if tmin < minima:
            minima = tmin
    return minima


def amplTerm(tabMeteo):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        res.append((data, tmax - tmin))
    return res


def maxChuva(tabMeteo):
    if len(tabMeteo) == 0:
        return None
    max_data = tabMeteo[0][0]
    max_prec = tabMeteo[0][3]
    for data, tmin, tmax, prec in tabMeteo:
        if prec > max_prec:
            max_data = data
            max_prec = prec
    return (max_data, max_prec)


def diasChuvosos(tabMeteo, p):
    res = []
    for data, tmin, tmax, prec in tabMeteo:
        if prec > p:
            res.append((data, prec))
    return res


def maxPeriodoCalor(tabMeteo, p):
    
    maior = 0
    atual = 0
    for data, tmin, tmax, prec in tabMeteo:
        if prec < p:
            atual = atual + 1
            if atual > maior:
                maior = atual
        else:
            atual = 0
    return maior


def grafTabMeteo(tabMeteo):
    if len(tabMeteo) == 0:
        print("A tabela meteorológica está vazia.")
    else:
        x = [dataTexto(data) for data, tmin, tmax, prec in tabMeteo]
        y_min = [tmin for data, tmin, tmax, prec in tabMeteo]
        y_max = [tmax for data, tmin, tmax, prec in tabMeteo]
        y_prec = [prec for data, tmin, tmax, prec in tabMeteo]

        plt.figure()
        plt.plot(x, y_min, marker="o", label="Temperatura mínima (ºC)")
        plt.plot(x, y_max, marker="o", label="Temperatura máxima (ºC)")
        plt.title("Temperaturas por dia")
        plt.xlabel("Data")
        plt.ylabel("Temperatura (ºC)")
        plt.legend()
        plt.grid()
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        plt.figure()
        plt.bar(x, y_prec, label="Precipitação (mm)")
        plt.title("Precipitação por dia")
        plt.xlabel("Data")
        plt.ylabel("Precipitação (mm)")
        plt.legend()
        plt.grid(axis="y")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


def mostrarPares(lista):
    if len(lista) == 0:
        print("Não existem resultados.")
    else:
        for data, valor in lista:
            print(f"({dataTexto(data)}, {valor})")


# Tabela apresentada na Aula P6.
tabMeteo = [
    ((2022, 1, 20), 2.0, 16.0, 0.0),
    ((2022, 1, 21), 1.0, 13.0, 0.2),
    ((2022, 1, 22), 7.0, 17.0, 0.01)
]

opcao = -1
while opcao != 0:
    menu()
    opcao_str = input("Selecione uma das opções: ")
    if opcao_str.isdigit():
        opcao = int(opcao_str)
    else:
        opcao = -1
        print("Opção inválida. Introduza um número do menu.")

    if opcao == 1:
        if len(tabMeteo) == 0:
            print("A tabela meteorológica está vazia.")
        else:
            print("Temperatura média de cada dia:")
            mostrarPares(medias(tabMeteo))

    elif opcao == 2:
        nomeFicheiro = input("Nome do ficheiro para guardar (ex.: meteorologia.txt): ")
        guardaTabMeteo(tabMeteo, nomeFicheiro)
        print("Tabela meteorológica guardada com sucesso.")

    elif opcao == 3:
        nomeFicheiro = input("Nome do ficheiro a carregar (ex.: meteorologia.txt): ")
        tabMeteo = carregaTabMeteo(nomeFicheiro)
        print("Tabela meteorológica carregada com sucesso.")
        print(f"Número de registos: {len(tabMeteo)}")

    elif opcao == 4:
        minima = minMin(tabMeteo)
        if minima is None:
            print("A tabela meteorológica está vazia.")
        else:
            print(f"A temperatura mínima mais baixa foi {minima} ºC.")

    elif opcao == 5:
        print("Amplitude térmica de cada dia:")
        mostrarPares(amplTerm(tabMeteo))

    elif opcao == 6:
        resultado = maxChuva(tabMeteo)
        if resultado is None:
            print("A tabela meteorológica está vazia.")
        else:
            data, prec = resultado
            print(f"Dia com precipitação máxima: {dataTexto(data)} — {prec} mm")

    elif opcao == 7:
        p_str = input("Introduza o limite de precipitação p (mm): ")
        s_limpo = p_str.lstrip('-')
        if s_limpo.count('.') <= 1 and s_limpo.replace('.', '').isdigit() and s_limpo != '':
            p = float(p_str)
            print(f"Dias com precipitação superior a {p} mm:")
            mostrarPares(diasChuvosos(tabMeteo, p))
        else:
            print("O limite tem de ser um número.")

    elif opcao == 8:
        p_str = input("Introduza o limite de precipitação p (mm): ")
        s_limpo = p_str.lstrip('-')
        if s_limpo.count('.') <= 1 and s_limpo.replace('.', '').isdigit() and s_limpo != '':
            p = float(p_str)
            print("Maior número consecutivo de dias com precipitação abaixo do limite:",
                  maxPeriodoCalor(tabMeteo, p))
        else:
            print("O limite tem de ser um número.")

    elif opcao == 9:
        grafTabMeteo(tabMeteo)

    elif opcao == 0:
        print("Obrigado por utilizar a aplicação.")

    elif opcao != -1:
        print("Resposta Inválida! Por favor selecione uma das opções.")