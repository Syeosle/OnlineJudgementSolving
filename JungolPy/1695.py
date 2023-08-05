n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

chk = grid[:]
apts = [0]


def f(x, y):
    chk[x][y] = 0
    if check(x-1, y): f(x-1, y)
    if check(x+1, y): f(x+1, y)
    if check(x, y-1): f(x, y-1)
    if check(x, y+1): f(x, y+1)



for i in range(n):
    for j in range(n):
        if not chk[i][j]:
            f(i, j)