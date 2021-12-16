N = int(input())
temp = list()
lista = []
for i in range(0, N):
    nums = list(map(float, input().split()))
    lista.append(nums)

pesos = [2, 3, 5]

for lista1 in lista:
    m = 0
    for pos, v in enumerate(lista1):
        m += pesos[pos] * v
    m /= sum(pesos)
    print(f'{m:.1f}')


