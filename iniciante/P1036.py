from math import sqrt
a, b, c = [float(x) for x in input().split(" ")]
try:
    d = b ** 2 - 4 * a * c
    r1 = (-b + sqrt(d)) / (2 * a)
    r2 = (-b - sqrt(d)) / (2 * a)
    print('R1 = {:.5f}'.format(r1))
    print('R2 = {:.5f}'.format(r2))
except ZeroDivisionError:
    print('Impossivel calcular')
except ValueError:
    print('Impossivel calcular')