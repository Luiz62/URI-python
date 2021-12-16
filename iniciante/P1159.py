s = 0
while True:
    X = int(input())
    if X == 0:
        break
    else:
        if not X % 2 == 0:
            X += 1
        s = 0
        for i in range(5):
            s += X
            X += 2
        print(s)
