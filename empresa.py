class Empresa:
    def __init__(self, listaFuncionarios):
        self._listaFuncionarios = listaFuncionarios
        self._funcionariologado = "Nenhum usuario logado"

    

    

    def loginFuncionario(self, login, senha):
        for funcionario in self._listaFuncionarios:
            if funcionario.getCargo() == "Gerente":
                if funcionario.getlogin() == login:
                    if funcionario.getSenha() == senha:
                        self._setfuncionariologado(funcionario)
                        print(f"Logado como{self._funcionariologado.getNome()}")
                        break

    def imprimirFuncionarios(self):
        print(self.listaFuncionarios)