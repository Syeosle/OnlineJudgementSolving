def is_cube_ok(i, j):
    a, b = i//3, j//3
    cnt = 0
    for i_ in range(3*a, 3*a+3):
        for j_ in range(3*b, 3*b+3):
            if grid[i_][j_] == grid[i][j]: cnt+=1
    if cnt == 1: return True
    return False


def is_row_ok(i, j):
    if grid[i].count(grid[i][j]) == 1: return True
    return False


def is_col_ok(i, j):
    cnt = 0
    for i_ in range(9):
        if grid[i_][j] == grid[i][j]: cnt+=1
    if cnt == 1: return True
    return False


def f(pos):
    now = pos
    while(now<81):
        i = now // 9
        j = now % 9
        if grid[i][j] == 0:
            for k in range(1, 10):
                grid[i][j] = k
                if is_col_ok(i, j) and is_row_ok(i, j) and is_cube_ok(i, j):
                    if f(now+1): return 1
            grid[i][j] = 0
            return 0
        now += 1
    return 1


grid = []

for _ in range(9):
    grid.append(list(map(int, input().split())))

f(0)

for i in range(9):
    for j in range(9):
        print(grid[i][j], end=' ')
    print()