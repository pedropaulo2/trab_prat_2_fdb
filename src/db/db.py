from typing import List, Tuple
import psycopg2

from leitor_csv.data_classes import Aluno, Disciplina, Historico, Professor, Turma


SQL_ALUNOS = """
    CREATE TABLE IF NOT EXISTS Alunos(
        mat INTEGER NOT NULL,
        nome VARCHAR(40) NOT NULL,
        semestre INTEGER NOT NULL,
        data_nasc DATE NOT NULL,
        PRIMARY KEY(mat)
    )
"""

SQL_DISCIPLINAS = """
    CREATE TABLE IF NOT EXISTS Disciplinas(
        cod_disc INTEGER NOT NULL,
        nome VARCHAR(70) NOT NULL,
        creditos INTEGER NOT NULL,
        PRIMARY KEY(cod_disc)
    )
"""

SQL_PROFESSORES = """
    CREATE TABLE IF NOT EXISTS Professores(
        cod_prof INTEGER NOT NULL,
        nome VARCHAR(40) NOT NULL,
        area_pesquisa VARCHAR(60) NOT NULL,
        PRIMARY KEY(cod_prof)
    )
"""

SQL_TURMAS = """
    CREATE TABLE IF NOT EXISTS Turmas(
        cod_turma INTEGER NOT NULL,
        cod_disc INTEGER NOT NULL,
        cod_prof INTEGER NOT NULL,
        ano VARCHAR(6) NOT NULL,
        horario VARCHAR(7) NOT NULL,
        PRIMARY KEY(cod_turma),
        CONSTRAINT fk_cod_disc FOREIGN KEY(cod_disc)
        REFERENCES Disciplinas(cod_disc) ON DELETE CASCADE,
        CONSTRAINT fk_cod_prof FOREIGN KEY(cod_prof)
        REFERENCES Professores(cod_prof) ON DELETE CASCADE
    )
"""

SQL_HISTORICO = """
    CREATE TABLE IF NOT EXISTS Historico(
        cod_hist INTEGER NOT NULL,
        mat INTEGER NOT NULL,
        cod_turma INTEGER NOT NULL,
        cod_disc INTEGER NOT NULL,
        cod_prof INTEGER NOT NULL,
        ano VARCHAR(6) NOT NULL,
        frequencia DECIMAL NOT NULL,
        nota DECIMAL NOT NULL,
        PRIMARY KEY(cod_hist),
        CONSTRAINT fk_mat FOREIGN KEY(mat) REFERENCES Alunos(mat) ON DELETE CASCADE
    )
"""


class DB:
    __HOST = "200.129.44.249"
    __DB = "473741"
    __USER = "fbd2021"
    __PASSWORD = "Ck0114"
    conn = None
    cursor = None

    @classmethod
    def conectar(cls) -> None:
        try:
            DB.conn = psycopg2.connect(
                host=DB.__HOST,
                database=DB.__DB,
                user=DB.__USER,
                password=DB.__PASSWORD,
            )

            cls.cursor = DB.conn.cursor()

        except Exception as e:
            print("Erro ao criar conexão! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def deletar_tudo(cls) -> None:
        try:
            cls.cursor.execute(
                """
                    DROP TABLE Historico;
                    DROP TABLE Turmas;
                    DROP TABLE Alunos;
                    DROP TABLE Disciplinas;
                    DROP TABLE Professores;
                """
            )
            cls.conn.commit()
        except Exception as e:
            print("Erro ao excluir dados! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def criar_tabelas(cls) -> None:
        try:
            cls.cursor.execute(SQL_ALUNOS)
            cls.cursor.execute(SQL_DISCIPLINAS)
            cls.cursor.execute(SQL_PROFESSORES)
            cls.cursor.execute(SQL_TURMAS)
            cls.cursor.execute(SQL_HISTORICO)
            cls.conn.commit()
        except Exception as e:
            print("Erro ao criar tabelas! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def inserir_alunos(cls, alunos: List[Aluno]):
        try:
            for aluno in alunos:
                cls.cursor.execute(
                    """
                        INSERT INTO Alunos(mat, nome, semestre, data_nasc)
                        VALUES (%s, %s, %s, %s);
                    """,
                    (aluno.matricula, aluno.nome, aluno.semestre, aluno.data_nasc)
                )
            cls.conn.commit()

        except Exception as e:
            print("Erro ao inserir alunos! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def inserir_disciplinas(cls, disciplinas: List[Disciplina]):
        try:
            for disciplina in disciplinas:
                cls.cursor.execute(
                    """
                        INSERT INTO Disciplinas(cod_disc, nome, creditos)
                        VALUES (%s, %s, %s);
                    """,
                    (disciplina.codigo_disc,
                     disciplina.nome_disciplina, disciplina.creditos)
                )
            cls.conn.commit()

        except Exception as e:
            print("Erro ao inserir disciplinas! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def inserir_professores(cls, professores: List[Professor]):
        try:
            for professor in professores:
                cls.cursor.execute(
                    """
                        INSERT INTO Professores(cod_prof, nome, area_pesquisa)
                        VALUES(%s, %s, %s);
                    """,
                    (professor.codigo_professor,
                     professor.nome, professor.area_pesquisa)
                )
            cls.conn.commit()

        except Exception as e:
            print("Erro ao inserir professores! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def inserir_turmas(cls, turmas: List[Turma]):
        try:
            for turma in turmas:
                cls.cursor.execute(
                    """
                        INSERT INTO Turmas(cod_turma, cod_disc, cod_prof, ano, horario)
                        VALUES(%s, %s, %s, %s, %s);
                    """,
                    (
                        turma.codigo_turma, turma.codigo_disc, turma.codigo_professor,
                        turma.ano, turma.horario
                    )
                )
            cls.conn.commit()

        except Exception as e:
            print("Erro ao inserir turmas! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def inserir_historico(cls, historicos: List[Historico]):
        try:
            for historico in historicos:
                cls.cursor.execute(
                    """
                        INSERT INTO Historico(
                            cod_hist, mat, cod_turma, cod_disc, cod_prof, ano, frequencia, nota
                        )
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                    """,
                    (
                        historico.codigo_historico, historico.matricula_aluno,
                        historico.codigo_turma, historico.codigo_disc,
                        historico.codigo_professor, historico.ano,
                        historico.frequencia, historico.nota)
                )
            cls.conn.commit()

        except Exception as e:
            print("Erro ao inserir historico! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def query(cls, sql, *vars) -> List[Tuple]:
        try:
            cls.cursor.execute(sql, vars or ())
            return cls.cursor.fetchall()
        except Exception as e:
            print(f"Erro ao realizar query='{sql}'! Erro: ", e)
            cls.conn.close()
            exit(1)

    @classmethod
    def fechar_conexao(cls):
        if not cls.conn.closed:
            cls.conn.close()


class Query:
    # Encontre a mat(matrícula) e nome dos alunos com nota em Fundamentos
    # de Banco de dados maior que 7.
    SQL_QUERY_1 = """
        SELECT a.mat, a.nome FROM Alunos a, Historico h, Disciplinas d
        WHERE a.mat = h.mat
        AND h.cod_disc = d.cod_disc
        AND d.nome = 'Fundamentos de Banco de Dados'
        AND h.nota = 7;
    """

    # Calcule a média das notas dos alunos na disciplina de Computação Gráfica.
    SQL_QUERY_2 = """
        SELECT AVG(h.nota) FROM Alunos a, Historico h, Disciplinas d
        WHERE a.mat = h.mat
        AND h.cod_disc = d.cod_disc
        AND d.nome LIKE 'Computação Gráfica%%';
    """

    # Retorne o nome dos alunos que tiveram a frequência menor que 0.75 e as
    # disciplinas relacionadas.
    SQL_QUERY_3 = """
        SELECT a.nome, d.nome FROM Alunos a, Historico h, Disciplinas d
        WHERE a.mat = h.mat
        AND h.cod_disc = d.cod_disc
        AND h.frequencia > 0.75;
    """

    # Imprima o nome dos professores da área de “Algoritmos e Otimização”
    # que dão/deram aula para pelo menos 5 alunos, independente do semestre.
    SQL_QUERY_4 = """
        SELECT p.nome FROM Professores p, Turmas t, Historico h
        WHERE p.area_pesquisa = 'Algoritmos e Otimização'
        AND p.cod_prof = h.cod_prof
        GROUP BY p.nome
        HAVING COUNT(h.mat) >= 5;
    """

    # Retorne o nome e a data de nascimento dos alunos que tiraram nota menor
    # que 5 na disciplina de Fundamentos de Bancos de Dados no semestre de 2021.1.
    SQL_QUERY_5 = """
        SELECT a.nome, a.data_nasc, h.ano FROM Alunos a, Disciplinas d, Historico h
        WHERE a.mat = h.mat
        AND h.nota < 5
        AND d.cod_disc = h.cod_disc
        AND h.ano = '2021.1'
        AND d.nome = 'Fundamentos de Banco de Dados';
    """
