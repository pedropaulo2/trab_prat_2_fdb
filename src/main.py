from db.db import DB, Query, Transaction
from leitor_csv.leitor_csv import LeitorCSV
from utils.print import print_rows


LeitorCSV.ler_dados()
DB.conectar()

reset = input("Resetar dados? [s/n] ")

if reset.lower() == "s":
    DB.deletar_tudo()
    DB.criar_tabelas()
    DB.inserir_alunos(LeitorCSV.alunos)
    DB.inserir_disciplinas(LeitorCSV.displinas)
    DB.inserir_professores(LeitorCSV.professores)
    DB.inserir_turmas(LeitorCSV.turmas)
    DB.inserir_historico(LeitorCSV.historico)

# Consulta
res = DB.query(Query.SQL_QUERY_1)
print_rows(
    res,
    label=(
        "\n\nEncontre a mat(matrícula) e nome dos alunos com nota em Fundamentos"
        "de Banco de dados maior que 7.\n"
    )
)
res = DB.query(Query.SQL_QUERY_2)
print_rows(
    res,
    label="\n\nCalcule a média das notas dos alunos na disciplina de Computação Gráfica.\n"
)
res = DB.query(Query.SQL_QUERY_3)
print_rows(
    res,
    label=(
        "\n\nRetorne o nome dos alunos que tiveram a frequência menor que 0.75 e as"
        "disciplinas relacionadas.\n"
    )
)
res = DB.query(Query.SQL_QUERY_4)
print_rows(
    res,
    label=(
        "\n\nImprima o nome dos professores da área de “Algoritmos e Otimização”"
        "que dão/deram aula para pelo menos 5 alunos, independente do semestre.\n"
    )
)
res = DB.query(Query.SQL_QUERY_5)
print_rows(
    res,
    label=(
        "\n\nRetorne o nome e a data de nascimento dos alunos que tiraram nota menor"
        "que 5 na disciplina de Fundamentos de Bancos de Dados no semestre de 2021.1.\n"
    )
)

# Transação
retorno = DB.transaction([Transaction.STATEMENT_1, Transaction.STATEMENT_2, Transaction.STATEMENT_3])
labels = [
    "\n\nInsere a seguinte tupla na tabela Alunos: (392889, Tiago, 3, 09/04/2001)\n",
    "\n\nInsere a seguinte tupla na tabela Histórico: (392889, 1, 1, 1, 2020.1, 0.90,8).\n",
    "\n\nEncontre a MAT(matrícula) e nome dos alunos com nota em Fundamentos de Banco de dados \nmaior que 8.\n"
]

i = 0
for res in retorno:    

    print_rows(
        res,
        label=(
            labels[i]
        )
    )
    i += 1

DB.fechar_conexao()
