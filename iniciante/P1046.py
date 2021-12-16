lista = []
valores = input().split()
for valor in valores:
    lista.append(int(valor))
h = 24
if lista[0] == 0 and lista[1] == 0:
    h = 24
elif lista[0] > lista[1]:
    h = 24 + lista[1] - lista[0]
elif lista[1] > lista[0]:
    h = lista[1] - lista[0]
print('O JOGO DUROU {} HORA(S)'.format(h))
