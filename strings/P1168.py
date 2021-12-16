def qual_valor(numero):
    v1 = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    r = 0
    for pos, valor in enumerate(v1):
        if numero == pos:
            r = valor
    return r


N = int(input())
lista = []
for i in range(N):
    num = str(input())
    x = 0
    for n1 in num:
        x += qual_valor(int(n1))
    lista.append(x)

for v in lista:
    print(v, 'leds')