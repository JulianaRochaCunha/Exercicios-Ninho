
from Controle.classConexao import Conexao
import psycopg2

try:
    con = Conexao("Empresa", "localhost", "5432", "postgres", "postgres")

    con.manipularBanco('''
    INSERT INTO "Funcionarios"
    Values(default, 'José')
    ''')

    print (con.consultarBanco('''
    SELECT *FROM "Funcionarios"
    '''))

    print(con.consultarBanco('''
    SELECT * FROM "Funcionarios"
    '''))

    con._db.close()


    
except (Exception, psycopg2.Error) as error:
    print("Ocorreu um erro:", error)
