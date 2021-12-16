def eh_multiplo_de_13(num):
    if num % 13 != 0:
        return True
    return False


x_y = [int(input()), int(input())]
temp = []

for i in range(min(x_y), max(x_y)+1):
    if eh_multiplo_de_13(i):
        temp.append(i)

print(sum(temp))