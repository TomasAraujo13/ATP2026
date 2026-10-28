# **ATP TPC6**


- **Nome**: Tomás Duarte Araújo
- **Id**: A113492
- **Foto**: ![alt text](image.png)

## **Aplicação de Metereologia**

O objetivo principal deste trabalho consistiu no desenvolvimento de uma aplicação interativa em Python, baseada num menu de opções, dedicada à gestão de uma tabela meteorológica. A aplicação foi desenvolvida para permitir ao utilizador gerir um conjunto de registos meteorológicos através de várias funcionalidades essenciais: calcular a temperatura média e a amplitude térmica de cada dia, determinar a temperatura mínima mais baixa, encontrar o dia com precipitação máxima, listar dias com precipitação superior a um limite, calcular o maior período consecutivo com precipitação abaixo de um limite, desenhar gráficos informativos das temperaturas e da pluviosidade, guardar e carregar a informação meteorológica em ficheiros de texto externos e, por fim, encerrar a aplicação.

O principal desafio neste trabalho consistiu na conceção da lógica algorítmica para percorrer a lista de registos e monitorizar as sequências de dias secos. Foi necessário criar variáveis de controlo para registar o período atual em curso e comparar com o maior período encontrado até ao momento. A complexidade aumentou porque, sempre que aparecia um dia cuja precipitação ultrapassava o limite estabelecido, o contador do período atual tinha de ser reiniciado a zero, enquanto o recorde máximo era atualizado condicionalmente. Esta gestão rigorosa dos ciclos e das condições exigiu um raciocínio lógico muito cuidadoso para garantir que a contagem dos dias consecutivos funcionava corretamente em qualquer cenário.

**Resolução:** [text](tpc6.py)