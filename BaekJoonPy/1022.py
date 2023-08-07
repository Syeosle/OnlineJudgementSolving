
r1, c1, r2, c2 = tuple(map(int, input().split()))


def num(r, c):
    level_r = (abs(r * 2 + 1) + 1) // 2
    level_c = (abs(c * 2 - 1) + 1) // 2
    level = level_c - 1 if level_c > level_r else level_r - 1

    if c - 1 < r < 1 - c:
        add = level + r + 1
    elif r > c - 2 and r > -c:
        add = 3 * level + c + 1
    elif c > r > -1 - c:
        add = 5 * level - r + 2
    else:
        add = 7 * level - c + 4

    return level * level * 4 + add


L = [[num(r, c) for c in range(c1, c2 + 1)] for r in range(r1, r2 + 1)]

digit = lambda x: (len(str(x)))
maxD = 0

for i in L:
    for j in i:
        d = digit(j)
        if d > maxD: maxD = d

for i in range(len(L)):
    for j in range(len(L[0])):
        print(f"{' '*(maxD - digit(L[i][j]))}{L[i][j]}", end='')
        if j < len(L[0])-1: print(' ', end='')
    print()
