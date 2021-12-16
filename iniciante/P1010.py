l1 = input().split(" ")
l2 = input().split(" ")
c1, n1, v1 = l1
c2, n2, v2 = l2

print(f'VALOR A PAGAR: R$ {(int(n1) * float(v1)) + (int(n2) * float(v2)):.2f}')