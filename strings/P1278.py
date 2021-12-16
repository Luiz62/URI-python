lista = []
temp = []
while True:
    N = int(input())
    if N == 0:
        break
    else:
        for i in range(N):
            frase = input().strip()
            x = frase.split()
            div = ' '.join(x)
            temp.append(div)
        lista.append(temp.copy())
        temp.clear()

for pos, valor in enumerate(lista):
    for valor1 in valor:
        maior = max(lista[pos], key=len)
        tamanho = len(maior)
        print(f'{valor1:>{tamanho}}')
    if pos != len(lista)-1:
        print('')