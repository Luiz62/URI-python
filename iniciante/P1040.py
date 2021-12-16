def situacao(media_def):
    if media_def >= 7:
        print(f'Media: {media:.1f}')
        print('Aluno aprovado.')
    elif media_def < 5.0:
        print(f'Media: {media:.1f}')
        print('Aluno reprovado.')
    else:
        nota = float(input())
        sla(nota, media_def)


def sla(h, h1):
    print(f'Media: {h1:.1f}')
    print('Aluno em exame.')
    print(f'Nota do exame: {h:.1f}')
    media_final = (h1 + h) / 2
    if media_final >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {media_final:.1f}')


valores = input().split()
lista = []
lista2 = [2, 3, 4, 1]
for pos, valor in enumerate(valores):
    lista.append(float(valor) * lista2[pos])
media = sum(lista) / sum(lista2)
situacao(media)
