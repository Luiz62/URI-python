x = 0
notas = []
while True:
    nota = float(input())
    if 0 <= nota <= 10:
        x += 1
        notas.append(nota)
        if x == 2:
            break
    else:
        print('nota invalida')

print('media = {:.2f}'.format(
    sum(notas) / len(notas)
))
