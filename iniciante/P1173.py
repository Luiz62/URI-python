lista = []

v = int(input())

for i in range(0, 10):
    lista.append(v)
    v *= 2

for pos, valor in enumerate(lista):
    print(f'N[{pos}] = {valor}')
