class Aluno:
    def __init__(self, matricula: str, nome: str, semestre: int, data_nasc: str) -> None:
        self.matricula = matricula
        self.nome = nome
        self.semestre = semestre
        self.data_nasc = data_nasc

    def __str__(self) -> str:
        return f"{self.matricula:^6} {self.nome:^20} {self.semestre:^2} {self.data_nasc:^10}"


class Disciplina:
    def __init__(self, codigo_disc: int, nome_disciplina: str, creditos: int) -> None:
        self.codigo_disc = codigo_disc
        self.nome_disciplina = nome_disciplina
        self.creditos = creditos

    def __str__(self) -> str:
        return f"{self.codigo_disc:^6} {self.nome_disciplina:^50} {self.creditos:^2}"


class Historico:
    def __init__(
            self,
            codigo_historico: int,
            matricula_aluno: int,
            codigo_turma: int,
            codigo_disc: int,
            codigo_professor: int,
            ano: float,
            frequencia: float,
            nota: float) -> None:

        self.codigo_historico = codigo_historico
        self.matricula_aluno = matricula_aluno
        self.codigo_turma = codigo_turma
        self.codigo_disc = codigo_disc
        self.codigo_professor = codigo_professor
        self.ano = ano
        self.frequencia = frequencia
        self.nota = nota

    def __str__(self) -> str:
        return (
            f"{self.codigo_historico:^3} {self.matricula_aluno:^6} {self.codigo_turma:^3}"
            f"{self.codigo_disc:^6} {self.codigo_professor:^3} {self.ano:^6}"
            f"{self.frequencia:^4} {self.nota:^3}")


class Professor:
    def __init__(self, codigo_professor: int, nome: str, area_pesquisa: str) -> None:
        self.codigo_professor = codigo_professor
        self.nome = nome
        self.area_pesquisa = area_pesquisa

    def __str__(self) -> str:
        return f"{self.codigo_professor:^3} {self.nome:^30} {self.area_pesquisa:^20}"


class Turma:
    def __init__(
            self,
            codigo_turma: int,
            codigo_disc: int,
            codigo_professor: int,
            ano: float,
            horario: str) -> None:
        self.codigo_turma = codigo_turma
        self.codigo_disc = codigo_disc
        self.codigo_professor = codigo_professor
        self.ano = ano
        self.horario = horario

    def __str__(self) -> str:
        return (f"{self.codigo_turma} {self.codigo_disc}"
                f"{self.codigo_professor} {self.ano} {self.horario}")
