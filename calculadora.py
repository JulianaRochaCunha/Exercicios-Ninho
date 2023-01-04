
def soma(numero1, numero2):
    return float(numero1) + float(numero2)

def subtracao(numero1, numero2):
    return float(numero1) - float(numero2)

def divisao(numero1, numero2):
    return float(numero1) / float(numero2)

def multiplicacao(numero1, numero2):
    return float(numero1) * float(numero2)

def calculadora(n1,n2,op):

    if (op == "+"):
        print(soma(n1,n2))

    elif (op == "-"):
        print(subtracao(n1,n2))

    elif (op == "/"):
        print(divisao(n1,n2))

    elif (op == "*"):
        print(multiplicacao(n1,n2))

    else:
        print("O usuario digitou uma operação inválida")
        global repetir
        repetir = True

repetir = True

while(repetir):
    repetir = False

    num1 = input("Escreva o numero 1: ")
    num2 = input("Escreva o numero 2: ")

    operador = input("Escreva o operador(+,-,/,*)")
    if (num1.isnumeric() and num2.isnumeric()):
        calculadora(num1,num2,operador)
    else:
        print("O usuário digitou números inválidos")

