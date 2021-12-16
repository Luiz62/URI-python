lista = []

for i in range(0, 100):
    lista.append(float(input()))

for pos, valor in enumerate(lista):
    if valor <= 10:
        print(f'A[{pos}] = {valor}')
