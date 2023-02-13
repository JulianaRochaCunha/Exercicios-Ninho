import psycopg2 

def createTableclientes(cur,conexao):

    cur.execute('''
    CREATE TABLE clientes(
    "id" int GENERATED ALWAYS AS IDENTITY,
    "Nome" varchar(255),
    "Cpf" char(11) UNIQUE NOT NULL,
    PRIMARY KEY("ID")
    );
    ''')
    conexao.commit()

def inserirClientes(cur,conexao):
    novoNome = input("Insira o nome do novo cliente: ")

    while True:
        novoCpf = input("Insira o CPF do novo cliente: ")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break
        
    cur.execute(f'''
    INSERT INTO "clientes"
    VALUES(default, '{novoNome}', '{novoCpf}')
    ''')
    conexao.commit()

def modificarCliente(cur,conexao):
    listarClientes(cur,conexao)
    idClientes = int(input("Digite o id do Cliente que deseja modificar: "))

    cur.execute(f'''
        SELECT * FROM clientes
        WHERE "id" = {idClientes}
    ''')
    print("Cliente escolhido:",cur.fetchone())

    novoNome = input("Digite o novo nome: ")

    while True:
        novoCpf = input("Insira o novo CPF do cliente: ")
        if len(novoCpf) != 11:
            print("Tamanho inválido, o cpf precisa conter 11 digitos")
        else:
            break

    cur.execute(f'''
    UPDATE clientes
    SET "nome" = '{novoNome}', "cpf" = '{novoCpf}'
    WHERE "id" = {idClientes}
    ''')
    conexao.commit()

def removerCliente(cur, conexao):
    listarClientes(cur,conexao)
    idClientes = int(input("Digite o id do cliente que deseja remover: "))
    cur.execute(f'''
        SELECT * FROM clientes
        WHERE "id" = {idClientes}
    ''')
    print("Cliente escolhido:",cur.fetchone())
    cur.execute(f'''
    DELETE FROM clientes
    WHERE "id" = {idClientes}
    ''')
    conexao.commit()

def listarClientes(cur, conexao):

    cur.execute('''
    SELECT * FROM "clientes"
    ''')
    clientes = cur.fetchall()
    print("id | Nome | CPF ")
    for cliente in clientes:
        print(f"{cliente[0]} | {cliente[1]} | {cliente[2]} ")


while True:
    try:

        con = psycopg2.connect(database="Biblioteca",user="postgres", password="postgres", host="localhost", port="5432")
        


        cursor = con.cursor()
        print("Conectado")

        print('''
        1. Ver Clientes
        2. Inserir Clientes
        3. Modificar Cliente
        4. Remover Cliente
        0. Finalizar
        ''')

        opcaoMenu = input("Escolha o que deseja fazer: ")

        match opcaoMenu:
            case "1":
                listarClientes(cursor, con)
            case "2":
                inserirClientes(cursor, con)
            case "3":
                modificarCliente(cursor, con)
            case "4":
                removerCliente(cursor, con)
            case "0":
                print("Você escolheu sair da aplicação. Até Logo!")
                break
            case _:
                print("Você inseriu algum valor inválido.")

        input("Tecle Enter para prosseguir")

        cursor.close()
        con.close()
    
    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro -", error)