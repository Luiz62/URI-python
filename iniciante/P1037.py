N = float(input())
if 25 >= N >= 0:
    print('Intervalo [0,25]')
elif 50 >= N > 25:
    print('Intervalo (25,50]')
elif 75 >= N > 50:
    print('Intervalo (50,75]')
elif 100 >= N > 75:
    print('Intervalo (75,100]')
else:
    print('Fora de intervalo')