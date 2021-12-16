valores = input().split()
lista = []
for valor in valores:
    lista.append(int(valor))

lista2 = lista.copy()
lista2.sort()

for valor in lista2:
    print(valor)
print()

for valor in lista:
    print(valor)
