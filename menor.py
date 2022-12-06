lista = []
qtd = input("informe a qtd de números: ")

for n in range(0,int(qtd)):
    lista.append(int(input("Digite o número: ")))

print("menor numero da lista: ",  min(lista))

