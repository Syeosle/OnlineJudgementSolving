n = int(input())
grid = []
for i in range(n):
    grid.append(list(map(int, input().split())))

chkpt = [1]*(2*n)
cnt, mx = 0, 0

#ind = row - col
def f(ind):
    global mx, cnt
    if mx == 2 * n - 2: return
    if ind == n:
        if mx < cnt: mx = cnt
        return
    flag = 1
    for row in range(max(0, ind), min(n, n + ind)):
        col = row - ind
        if grid[row][col] and chkpt[row + col]:
            chkpt[row + col] = 0; cnt += 1
            f(ind + 1)
            chkpt[row + col] = 1; cnt -= 1
            flag = 0
    if flag: f(ind + 1)



f(-n+1)

print(mx)