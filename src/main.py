from db.db import DB
from leitor_csv.leitor_csv import LeitorCSV

LeitorCSV.ler_dados()

DB.conectar()
DB.deletar_tudo()
DB.criar_tabelas()
DB.inserir_alunos(LeitorCSV.alunos)
DB.inserir_disciplinas(LeitorCSV.displinas)
DB.inserir_professores(LeitorCSV.professores) 
DB.inserir_turmas(LeitorCSV.turmas)
DB.inserir_historico(LeitorCSV.historico)