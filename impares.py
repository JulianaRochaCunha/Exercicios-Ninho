palavra=input("Escreva uma palavra")
impares = []
for i in range (len(palavra)):
    if(i%2 == 0):
        impares.append(palavra[i])
        print(impares)