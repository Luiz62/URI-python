def form(sla):
    pqp = sla
    if int(sla) != 0:
        if int(sla) % sla == 0:
            pqp = int(sla)
    return pqp


v = [0, 0, 0]
v1 = [1, 2, 3]
s = 0
while s < 2:
    for pos, x1 in enumerate(v1):
        j, h = round(v[pos]+s, 2), round(x1+s, 2)
        print(f'I={form(j)} J={form(h)}')
    s += 0.2
