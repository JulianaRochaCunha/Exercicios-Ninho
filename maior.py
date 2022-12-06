lista = []
qtd = input('informe a qtd de numeros: ')

for n in range(0,int(qtd)): 
    lista.append(int(input('Digite o número: ')))

print ('Maior número da lista: ', max(lista))    