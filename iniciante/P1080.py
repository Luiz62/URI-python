lista = []

for i in range(0, 100):
    lista.append(int(input()))

maior = max(lista)
print(maior)
print(lista.index(maior)+1)