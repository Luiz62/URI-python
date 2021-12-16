N = int(input())
v1 = ['o', 'n', 'e']
v2 = ['t', 'w', 'o']
lista = []
for i in range(N):
    num = str(input())
    if len(num) == 5:
        lista.append('3')
    else:
        um = dois = 0
        for j in range(0, 3):
            if num[j] == v1[j]:
                um += 1
            elif num[j] == v2[j]:
                dois += 1
        if um > dois:
            lista.append('1')
        else:
            lista.append('2')

for v in lista:
    print(v)
