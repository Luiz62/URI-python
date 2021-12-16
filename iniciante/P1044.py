valores = input().split()
lista = []
for valor in valores:
    lista.append(int(valor))
maior = max(lista)
menor = min(lista)
if maior % menor == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')