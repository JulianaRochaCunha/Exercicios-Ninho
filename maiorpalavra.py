frase = input('Digite a frase: ').split()
tam_palavras = list()
for palavra in frase:
    tam_palavras.append(len(palavra))

maior = max(tam_palavras)
print('Maior(es) palavra(s):')
for a, b in zip(frase, tam_palavras):
    if b == maior:
        print(a)