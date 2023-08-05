def d(n):
    for i in str(n):
        n += int(i)
    return n


L = list(range(1, 10000))

for i in range(1, 10000):
    j = d(i)
    if j<10000:
        if L[j-1] != 0:
            while (j < 10000):
                L[j-1] = 0
                j = d(j)

for i in L:
    if i != 0: print(i)