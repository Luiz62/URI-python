dic = {'1': 4, '2': 4.50, '3': 5,
       '4': 2, '5': 1.50}
valores = input().strip()
cod = valores[0]
qt = int(valores[2])
total = dic[cod] * qt
print(f'Total: R$ {total:.2f}')