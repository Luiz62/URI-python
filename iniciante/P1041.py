valores = input().split()
dic = {'X': float(valores[0]), 'Y': float(valores[1])}
if dic['X'] == 0 and dic['Y'] == 0:
    print('Origem')
elif dic['X'] == 0:
    print('Eixo Y')
elif dic['Y'] == 0:
    print('Eixo X')
elif dic['X'] > 0 and dic['Y'] > 0:
    print('Q1')
elif dic['X'] < 0 and dic['Y'] < 1:
    print('Q3')
elif dic['X'] > 0 > dic['Y']:
    print('Q4')
elif dic['X'] <= 0 <= dic['Y']:
    print('Q2')