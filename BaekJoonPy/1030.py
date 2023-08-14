s, n, k, r1, r2, c1, c2 = map(int, input().split())
k1, k2 = (n - k) // 2, (n - k) // 2 + k
grid = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
u = n**(s-1)


def col(r, c):
    tmp = u
    for _ in range(s):
        if k1 <= r//tmp % n < k2 and k1 <= c//tmp % n < k2: return 1
        tmp //= n
    return 0


for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(col(i, j), end='')
    print()
