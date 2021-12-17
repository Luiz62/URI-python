from random import choice
v1 = int(input("Digite um valor: "))
v2 = int(input("Digite um outro valor: "))
v3 = int(input("Digite um novamente um outro valor: "))

lista = [v1, v2, v3]

maior = max(lista)
menor = min(lista)

print(f"O maior valor foi {maior}")
print(f"O menor valor foi {menor}")
