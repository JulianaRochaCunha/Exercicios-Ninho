import psycopg2

def createTableFuncionario(cur,conexao):

    cur.execute('''
    CREATE TABLE "Funcionarios"(
    "ID" serial,
    "Nome" varchar(255),
    "CPF" char(11) NOT NULL,
    "Salário" money DEFAULT 0.00,
    PRIMARY KEY("ID")
    );

    ''')
    conexao.commit()


def inserirFuncionario(cur, conexao):
    novoNome = input("Insira o nome de um novo funcionario:")

    while True:
        novoCpf = input("Insira o CPF do novo funcionário: ")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break
    
    novoSalario = input("Insira o salario do novo funcionario:")

    cur.execute('''
    INSERT INTO "Funcionarios"
    VALUES(default, 'José Cleber', '12345678910', default)
    ''')
    conexao.commit()

def atualizarFuncionario(cur, conexao):
    idFunc = int(input("Digite o id do funcionario que deseja modificar:"))
    novoNome = input("Digite o novo nome")
    cur.execute(f'''
    UPDATE "Funcionarios"
    SET "Nome" = '{novoNome}'
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()

def removerFuncionario(cur, conexao):
    idFunc = int(input("Digite o id do funcionario que deseja remover:"))
    cur.execute(f'''
    DELETE FROM "Funcionarios"
    WHERE "ID" = {idFunc}
    ''')
    conexao.commit()

def listarFuncionario(cur, conexao):

    cur.execute('''
    SELECT * FROM "Funcionarios"
    ''')
    print(cur.fetchall())

while True:

    try:

        con = psycopg2.connect(database="Empresa",user="postgres",password="postgres",host="localhost",port="5432")

        cursor = con.cursor()
        print("Conectado")
        print('''
        1. Ver funcionários
        2. Inserir Funcionário
        3. Modificar Funcionário
        4. Remover Funcionário
        0. Sair do Programa
        ''')

        opcaoMenu = input("Escolha o que deseja fazer:")

        match opcaoMenu:
            case "1":
                listarFuncionario(cursor, con)
            case "2":
                inserirFuncionario(cursor, con)
            case "3":
                atualizarFuncionario(cursor, con)
            case "4":
                removerFuncionario(cursor, con)
            case "0":
                print("Voce escolheu sair da aplicação. Até mais!!")
                break
            case _:
                print("Voce digitou algum valor inválido.")

        input("Tecle Enter para prosseguir")

        cursor.close()
        con.close()
    
        '''atualizarFuncionario(cursor, conexao)
        cursor.close()
        conexao.close()
        print("Funcionario atualizado")'''

       '''listarFuncionario(cursor, con)
        cursor.close()
        con.close()'''

        

    except(Exception,psycopg2.Error) as error:

        
    print("Ocorreu um erro -", error)