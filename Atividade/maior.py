listanum = []
mai = 0
for c in range(0, 9):
    listanum.append(int(input(f'Digite m valor para a posição {c}: ')))
    if c == 0:
        mai = listanum[c]

print(f"Você digitou os valores {listanum}")
print(f"O maior valor digitado foi {mai}")


