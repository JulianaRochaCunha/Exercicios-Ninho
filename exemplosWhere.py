
if __name__ == "__main__":
    import psycopg2
    from Controle.classConexao import Conexao
    try:
        con = Conexao(parametroDb="Empresa", parametroHost="LocalHost", parametroPort="5432", parametroUser="postgres", parametroPassword="postgres")

        Funcionarios = con.consultarBanco('''
        SELECT * FROM "Funcionarios"
        ORDER BY "ID" ASC
        ''')

        print(Funcionarios)

        for funcionario in Funcionarios:
            print(f'''
            {funcionario[0]} - {funcionario[1]} - {funcionario[2]} - {funcionario[3]}
            ''')

        funcionario = con.consultarBanco('''
        SELECT * FROM "Funcionarios"
        WHERE "ID" = 1;
        ''')
        print("Pesquisa por ID:", funcionario)


        funcionario = con.consultarBanco('''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" = 'Claudia';
        ''')
        print("Pesquisa por Nome:", funcionario)


        print("Pesquisa por Salario maior:", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" > '2500'
        ORDER BY "ID";
        '''))

        print("Pesquisa por salario menor:", con. consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" < '3000'
        ORDER BY "ID";
        '''))

        print("Pesquisa por maior ou igual:", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" >= '2500'
        ORDER BY "ID";
        '''))

        print("Pesquisa por nome diferente:", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" <> 'Jose'
        ORDER BY "ID";
        '''))

        print("Pesquisa por salario entre valor:", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Salario" BETWEEN '2500' and '3000'
        ORDER BY "ID";
        '''))

        print("Pesquisa por lista de nomes:", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" in ('Joao Miguel', 'José', 'Claudia')
        ORDER BY "ID";
        '''))

        print("Pesquisa por nome:", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" LIKE '%Jo%'
        ORDER BY "ID";
        '''))

        print("Pesquisa por nome:", con.consultarBanco(f'''
        SELECT * FROM "Funcionarios"
        WHERE "Nome" NOT IN ('José', 'Claudia') 
        '''))

        con.fechar()

    except(Exception, psycopg2.Error) as error:
        print("Ocorreu um erro", error)

        