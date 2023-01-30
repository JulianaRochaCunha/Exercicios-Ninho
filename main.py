
import psycopg2

def createTableFuncionarios(cursor,conexao):
    cursor.execute('''
    DROP TABLE IF EXISTS "Funcionarios";

    CREATE TABLE "Funcionarios"(
        "ID" int GENERATED ALWAYS AS IDENTITY,
        "Nome" Varchar(255) NOT NULL,
        "Salario" money,
        "ID_Departamento" int,
        CONSTRAINT fk_departamento
            FOREIGN KEY("ID_Departamento")
            REFERENCES "Departamento"("ID")
            ON DELETE NO ACTION
            ON UPDATE NO ACTION,
            
        PRIMARY KEY ("ID"));
        ''')
    conexao.commit()

def createTableDepartamentos(cursor,conexao):
    cursor.execute('''
    DROP TABLE IF EXISTS "Departamentos";
    CREATE TABLE "Departamentos"(
        "ID" INT GENERATED ALWAYS AS IDENTITY,
        "Nome" Varchar(255) NOT NULL, 
        PRIMARY KEY("ID"));''')

def inserirFuncionario(cursor,conexao):
    
    cursor.execute('''
    INSERT INTO "Funcionarios"
    VALUES(default, 'Joao Miguel', '2.500,00', default)
    ''')
    conexao.commit()

try:

    con = psycopg2.connect(database="Empresa", user="postgres", password="postgres", host="localhost", port="5432")
    cursor = con.cursor()

    """createTableDepartamentos(cursor,con)
    print("Tabela Departamentos criada")

    createTableFuncionario(cursor,con)
    cursor.close()
    con.close()
    print("Tabela Funcionario criada")"""

   
    inserirFuncionario(cursor,con)
    cursor.close()
    con.close()

    print("Funcionario inserido")




except(Exception, psycopg2.Error) as error:

    print("Ocorreu um erro", error)
    
