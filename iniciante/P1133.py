def eh_5_2_3(num):
    if num % 5 == 2 or num % 5 == 3:
        return True


valores = [int(input()), int(input())]

for v in range(min(valores) + 1, max(valores)):
    if eh_5_2_3(v):
        print(v)
