def z(n, r, c):
    if n == 0: return 0

    lower = pow(2, n - 1)
    lower_cube = lower * lower
    next_r, next_c = r, c
    res = 0

    if r >= lower:
        next_r -= lower
        res += 2 * lower_cube
    if c >= lower:
        next_c -= lower
        res += lower_cube

    return res + z(n - 1, next_r, next_c)


n, r, c = map(int, input().split())
print(z(n, r, c))