palavra=input("Escreva uma palavra")
print(palavra[::-1])
palavrainvertida = ''
for i in range (len(palavra)):
    palavrainvertida += palavra [(len(palavra) -1) -i]
print("palavrainvertida")