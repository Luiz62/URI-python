N = int(input())
print(N)
notas = [100, 50, 20, 10, 5, 2, 1]
notas_nome = ['R$ 100,00', 'R$ 50,00', 'R$ 20,00',
              'R$ 10,00', 'R$ 5,00', 'R$ 2,00', 'R$ 1,00']
troco = [0, 0, 0, 0, 0, 0, 0]
f = 1
pos = 0
while True:
    if N >= notas[pos]:
        troco[pos] = N // notas[pos]
        N = N % notas[pos]
    else:
        pos += 1
    if pos >= len(notas):
        break

for i in range(0, 7):
    print(f'{troco[i]} nota(s) de {notas_nome[i]}')
