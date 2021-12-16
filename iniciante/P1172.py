lista = []

for i in range(0, 10):
    valor = int(input())

    if valor <= 0:
        lista.append(1)
    else:
        lista.append(valor)

for pos, v in enumerate(lista):
    print(f'X[{pos}] = {v}')
