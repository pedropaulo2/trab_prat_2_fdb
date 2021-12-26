from csv import reader

from typing import List
from data_classes import Aluno, Disciplina, Historico, Professor, Turma


class LeitorCSV:

    alunos: List[Aluno] = []
    displinas: List[Disciplina] = []
    historico: List[Historico] = []
    professores: List[Professor] = []
    turmas: List[Turma] = []

    @staticmethod
    def ler_dados():
        LeitorCSV.ler_csv_alunos()
        LeitorCSV.ler_csv_disciplinas()
        LeitorCSV.ler_csv_historico()
        LeitorCSV.ler_csv_professores()
        LeitorCSV.ler_csv_turmas()

    @staticmethod
    def __ler_csv_alunos():
        with open("data/Alunos.csv", encoding="utf-8") as file:
            csv_reader = reader(file)
            csv_reader.__next__()  # pulando a primeira linha do arquivo
            for line in csv_reader:
                matricula, nome, semestre, data_nasc = line[0], line[1], line[2], line[3]
                LeitorCSV.alunos.append(
                    Aluno(matricula, nome, semestre, data_nasc))

    @staticmethod
    def ler_csv_disciplinas():
        with open("data/Disciplinas.csv", encoding="utf-8") as file:
            csv_reader = reader(file)
            csv_reader.__next__()  # pulando a primeira linha do arquivo
            for line in csv_reader:
                codigo_disc, nome_disc, creditos = line[0], line[1], line[2]
                LeitorCSV.displinas.append(Disciplina(
                    codigo_disc, nome_disc, creditos))

    @staticmethod
    def ler_csv_historico():
        with open("data/Historico.csv", encoding="utf-8") as file:
            csv_reader = reader(file)
            csv_reader.__next__()  # pulando a primeira linha do arquivo
            for line in csv_reader:
                codigo_historico = line[0]
                matricula_aluno = line[1]
                codigo_turma = line[2]
                codigo_disc = line[3]
                codigo_professor = line[4]
                ano = line[5]
                frequencia = line[6]
                nota = line[7]
                LeitorCSV.historico.append(
                    Historico(
                        codigo_historico, matricula_aluno, codigo_turma,
                        codigo_disc, codigo_professor, ano, frequencia, nota
                    )
                )

    @staticmethod
    def ler_csv_professores():
        with open("data/Professores.csv", encoding="utf-8") as file:
            csv_reader = reader(file)
            csv_reader.__next__()  # pulando a primeira linha do arquivo
            for line in csv_reader:
                codigo_professor, nome, area_pesquisa = line[0], line[1], line[2]
                LeitorCSV.professores.append(
                    Professor(codigo_professor, nome, area_pesquisa))

    @staticmethod
    def ler_csv_turmas():
        with open("data/Turmas.csv", encoding="utf-8") as file:
            csv_reader = reader(file)
            csv_reader.__next__()  # pulando a primeira linha do arquivo
            for line in csv_reader:
                codigo_turma, codigo_disc, codigo_professor, ano, horario = line[
                    0], line[1], line[2], line[3], line[4]
                LeitorCSV.turmas.append(
                    Turma(codigo_turma, codigo_disc, codigo_professor, ano, horario))
