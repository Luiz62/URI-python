nome = str(input())
salario = float(input())
vendas = float(input())
final = (vendas * 0.15) + salario
print('TOTAL = R$ {:.2f}'.format(final))