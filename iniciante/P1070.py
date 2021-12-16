X = int(input())
c = 1
if X % 2 == 0:
    c = 0
    X += 1
for i in range(6):
    if c == 0:
        print(X)
        X += 2
    else:
        print(X)
        X += 2