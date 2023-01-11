
class Funcionario:
    def __init__(self, id, nome, cpf, salario):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome


    def getCpf(self):
        return self._cpf
    def setCpf(self,cpf):
        self._cpf = cpf

    def getSalario(self):
        return self._salario
    def setSalario(self,salario):
        self._salario = salario


funcionario1 = Funcionario(id=2, nome="Joao", cpf="00022255519", salario="1500")
funcionario2 = Funcionario(id=5, nome="Maria", cpf="25323855578", salario="2000")

print(funcionario1.getId())
print(funcionario1.getNome())
print(funcionario1.getCpf())
print(funcionario1.getSalario())

print(funcionario2.getId())
print(funcionario2.getNome())
print(funcionario2.getCpf())
print(funcionario2.getSalario())

class Gerente:
    def __init__(self, id, nome, cpf, login, senha):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._login = login
        self._senha = senha

    def getId(self):
        return self._id
    def setId(self, id):
        self._id = id

    def getNome(self):
        return self._nome
    def setNome(self,nome):
        self._nome = nome


    def getCpf(self):
        return self._cpf
    def setCpf(self,cpf):
        self._cpf = cpf

    def getLogin(self):
        return self._login
    def setLogin(self,login):
        self._login = login

    def getSenha(self):
        return self._senha
    def setSenha(self,senha):
        self._senha = senha




gerente1 = Gerente(id=3, nome= "Manuela", cpf= "55523688898", login= "Manu", senha= "23a")

print(gerente1.getId())
print(gerente1.getNome())
print(gerente1.getCpf())
print(gerente1.getLogin())
print(gerente1.getSenha())

login= input("Digite o seu login")
senha= input("Digite a sua senha")

if gerente1.getLogin==login:
    if gerente1.getsenha==senha:

        print("Você esta logado")


        