A = int(input("Digite o primeiro número"))
B = int(input("Digite o segundo número"))
C = int(input("Digite o terceiro número"))
maior = A
if B > A and B > C:
    maior = B
if C > A and C > B:
    maior = C
menor = A
if B < C and B < A:
    menor = B
if C < B and C< A:
    menor = C
print(f"O menor número digitado foi {menor}")
print(f"O maior número digitado foi {maior}")