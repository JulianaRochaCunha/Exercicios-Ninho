peso = float(input("Qual é o seu peso? (Kg) "))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura ** 2)
print("O imc dessa pessoa é de {}" . format(imc))
if imc <= 18:
    print("Você esta abaixo do peso")
if imc > 18 and imc < 25:
    print("Você esta no peso ideal")
if imc >=25 and imc <=30:
    print("Você esta com sobrepeso")
if imc > 30:
    print("Você esta com obesidade")