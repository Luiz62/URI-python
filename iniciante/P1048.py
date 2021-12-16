salario = float(input())
reajuste = 0
if 0 <= salario <= 400.00:
    reajuste = 15
elif 400.01 <= salario <= 800.00:
    reajuste = 12
elif 800.01 <= salario <= 1200.00:
    reajuste = 10
elif 1200.01 <= salario <= 2000.00:
    reajuste = 7
elif salario > 2000:
    reajuste = 4

reajuste_ganho = salario * reajuste / 100
novo_salario = salario + reajuste_ganho
print(f'Novo salario: {novo_salario:.2f}')
print(f'Reajuste ganho: {reajuste_ganho:.2f}')
print(f'Em percentual: {reajuste:.0f} %')