X = int(input())
Y = int(input())
s = i = 0
while Y <= X and Y != X:
    if Y % 2 != 0 and i != 0:
        s += Y
    Y += 1
    i += 1
print(s)