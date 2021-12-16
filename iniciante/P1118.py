x = 0
notas = []
while True:
    nota = float(input())
    if 0 <= nota <= 10:
        x += 1
        notas.append(nota)
        if len(notas) == 2:
            print('media = {:.2f}'.format(
                sum(notas) / len(notas)
            ))
            notas.clear()
        if x == 2:
            while True:
                co = str(input('novo calculo (1-sim 2-nao)\n'))
                if co == '1' or co == '2':
                    break
            if co == '2':
                break
            else:
                x = 0
    else:
        print('nota invalida')
