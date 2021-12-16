N = int(input())
temp = []
lista = []
h = 2
v = 1
for i in range(N):
    x = 1
    for j in range(3):
        temp.append(pow(v, x))
        x += 1
    lista.append(temp.copy())
    temp.clear()
    v = h
    h += 1

for pos, v in enumerate(lista):
    print(f'{lista[pos][0]} {lista[pos][1]} {lista[pos][2]}')