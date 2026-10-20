# **ATP TPC5**


- **Nome**: Tomás Duarte Araújo
- **Id**: A113492
- **Foto**: ![alt text](image.png)

## **Aplicação para a gestão de alunos **

O objetivo principal deste trabalho consistiu no desenvolvimento de uma aplicação interativa em Python, baseada num menu de opções, dedicada à gestão de uma turma de alunos. A aplicação foi desenvolvida para permitir ao utilizador gerir um conjunto de dados académicos através de várias funcionalidades essenciais: inserir novos alunos na turma (com nome, número de identificação e notas relativas a TPC, Projeto e Teste), listar todos os alunos registados, consultar a informação detalhada de um aluno através do seu ID, guardar e carregar a informação da turma em ficheiros de texto externos e, por fim, encerrar a aplicação.

A etapa em que senti mais dificuldades foi no desenvolvimento das opções de guardar e carregar a turma.
O principal desafio residiu na gestão e armazenamento de dados em ficheiros. Foi necessário garantir a correta delimitação dos campos ao exportar a informação para o ficheiro .txt, assim como assegurar o seu processamento inverso. Na fase de leitura, foi necessário remover a quebra de linha e dividir a frase pelos delimitadores de modo a isolar os vários campos do aluno. Por fim, como os dados lidos do ficheiro são sempre interpretados como texto, tornou-se indispensável converter individualmente as notas de string para números decimais.

**Resolução:** [text](tpc5.py)
