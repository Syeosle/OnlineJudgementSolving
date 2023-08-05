'''
n = int(input())
g = [0] * n


def dfs(cnt, d):
    if d > -1:
        if g.index(g[d]) != d: return cnt
        for i in range(d):
            dif = abs(g[i] - g[d])
            if d - i == dif: return cnt

    if d == n - 1: return cnt + 1

    for i in range(n):
        g[d + 1] = i
        cnt = dfs(cnt, d + 1)
    return cnt


print(dfs(0, -1))
'''

def f(row):
    if row>=n:return 1
    ret = 0
    for col in range(n):
        if col_chk[col] or d1_chk[col+row] or d2_chk[col-row+n]: continue
        col_chk[col] = d1_chk[col + row] = d2_chk[col - row + n] = 1
        ret += f(row+1)
        col_chk[col] = d1_chk[col + row] = d2_chk[col - row + n] = 0
    return ret


n = int(input())
col_chk = [0]*n
d1_chk = [0]*(n*2)
d2_chk = [0]*(n*2)
print(f(0))