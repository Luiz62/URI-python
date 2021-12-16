N = int(input())
tot = 0
t_c = t_r = t_s = 0
for i in range(0, N):
    valores = input().split()
    t = int(valores[0])
    tot += t
    tipo = str(valores[1])
    if tipo == 'C':
        t_c += t
    elif tipo == 'R':
        t_r += t
    elif tipo == 'S':
        t_s += t

print(f'Total: {tot} cobaias')
print(f'Total de coelhos: {t_c}')
print(f'Total de ratos: {t_r}')
print(f'Total de sapos: {t_s}')
print(f'Percentual de coelhos: {t_c*100/tot:.2f} %')
print(f'Percentual de ratos: {t_r*100/tot:.2f} %')
print(f'Percentual de sapos: {t_s*100/tot:.2f} %')
