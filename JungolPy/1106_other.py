near = [[0, 3, 2, 3, 2, 3, 0, 0, 3, 2, 3, 2, 3],
        [3, 2, 1, 2, 3, 0, 3, 3, 0, 3, 2, 1, 2],
        [2, 1, 0, 3, 2, 3, 0, 0, 3, 2, 3, 0, 1],
        [3, 2, 3, 2, 3, 0, 3, 3, 0, 3, 2, 3, 2],
        [2, 3, 2, 3, 0, 3, 0, 0, 3, 0, 3, 2, 3],
        [3, 0, 3, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0],
        [0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3],
        [0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3],
        [3, 0, 3, 0, 3, 0, 0, 0, 0, 3, 0, 3, 0],
        [2, 3, 2, 3, 0, 3, 0, 0, 3, 0, 3, 2, 3],
        [3, 2, 3, 2, 3, 0, 3, 3, 0, 3, 2, 3, 2],
        [2, 1, 0, 3, 2, 3, 0, 0, 3, 2, 3, 0, 1],
        [3, 2, 1, 2, 3, 0, 3, 3, 0, 3, 2, 1, 2]]


n, m = map(int, input().split())
r, c, s, k = map(int, input().split())
cnt = 0


def f(x, y):
    global cnt
    dx = s-x
    dy = k-y
    adx = abs(dx)
    ady = abs(dy)

    if adx < 7 and ady < 7 and near[dx][dy] != 0:
        return cnt + near[dx][dy]

    if adx > ady:
        if dx == adx: next_x = x + 2
        else: next_x = x - 2
        if dy == ady: next_y = y + 1
        else: next_y = y - 1
    else:
        if dx == adx: next_x = x + 1
        else: next_x = x - 1
        if dy == ady: next_y = y + 2
        else: next_y = y - 2

    cnt += 1
    return f(next_x, next_y)


if r == s and c == k: print(0)
else: print(f(r, c))