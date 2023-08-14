from math import sqrt
x, y, d, t = map(int, input().split())

if d <= t: print(sqrt(x*x+y*y))
else:
    cs = [sqrt(x * x + y * y)]
    cs += [cs[0]//d * t + cs[0] % d, (cs[0]//d + 1) * t + d - (cs[0] % d)]
    cs.append(max(cs[0]//d + 1, 2) * t)
    print(min(cs))
