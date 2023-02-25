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

'''CREATE TABLE livros
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    nome character varying(255) COLLATE pg_catalog."default",
    autor character varying(255) COLLATE pg_catalog."default",
    CONSTRAINT livros_pkey PRIMARY KEY (id)'''

def inserirLivros(cur,conexao):
    novoNome = input("Insira o nome do novo livro: ")
    novoAutor = input("Insira o nome do Autor do livro:")

    cur.execute(f'''
    INSERT INTO "livros"
    VALUES(default, '{novoNome}', '{novoAutor}')    
    ''')
    conexao.commit()
 
def listarLivros(cur, conexao):

    cur.execute('''
    SELECT * FROM "livros"
    ''')
    livros = cur.fetchall()
    print("id | Nome | Autor ")
    for livro in livros:
        print(f"{livro[0]} | {livro[1]} | {livro[2]} ")

def modificarLivros(cur,conexao):
    listarLivros(cur,conexao)
    idLivros = int(input("Digite o id do Livro que deseja modificar: "))

    cur.execute(f'''
        SELECT * FROM livros
        WHERE "id" = {idLivros}
    ''')
    print("Livro escolhido:",cur.fetchone())

    novoNome = input("Digite o novo nome: ")
    novoAutor = input("Digite o novo autor: ")
    
    cur.execute(f'''
    UPDATE Livros
    SET "nome" = '{novoNome}', "autor" = '{novoAutor}'
    WHERE "id" = {idLivros}
    ''')
    conexao.commit()


'''CREATE TABLE aluguel
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY,
    id_clientes integer NOT NULL,
    id_livros integer NOT NULL,
    CONSTRAINT aluguel_pkey PRIMARY KEY (id),
    CONSTRAINT fk_clientes FOREIGN KEY (id_clientes)
        REFERENCES public.clientes (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE,
    CONSTRAINT fk_livro FOREIGN KEY (id_livros)
        REFERENCES public.livros (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE SET NULL
)'''

def inserirAluguel(cur,conexao):
    idClientes = int(input("Digite o nome do Cliente"))
    idLivros = int(input("Digite o nome do Livro"))
    cur.execute(f'''
    INSERT INTO "aluguel"
    VALUES(default, '{idClientes}', '{idLivros}')

    ''')
    conexao.commit()



while True:
    try:

        con = psycopg2.connect(database="Ninho",user="postgres", password="postgres", host="localhost", port="5432")
        


        cursor = con.cursor()
        print("Conectado")

        print('''
        1. Ver Clientes
        2. Inserir Clientes
        3. Modificar Cliente
        4. Remover Cliente
        5. Inserir Aluguel
        6. Inserir Livros
        7. Ver Livros
        8. Modificar Livros
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
            case "5":
                inserirAluguel(cursor,con)
            case "6":
                inserirLivros(cursor,con)
            case "7":
                listarLivros(cursor,con)
            case "8":
                modificarLivros(cursor,con)
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
