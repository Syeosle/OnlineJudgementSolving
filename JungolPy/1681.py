def f(pos):
    global mn
    if pos == n:
        if now[n] < mn: mn = now[n]
        return
    for i in range(n):
        if i == 0 and pos < n-1 or cost[task[pos]][i] == 0: continue
        tmp = now[pos] + cost[task[pos]][i]
        if used[i] or mn <= tmp: continue
        now[pos+1] = tmp
        task[pos+1] = i
        used[i] = 1
        f(pos+1)
        used[i] = 0
        now[pos+1] = 0



n, cost = int(input()), []
for _ in range(n):
    cost.append(list(map(int, input().split())))


mn, now = 1300, [0]*(n+1)
task = [0]*(n+1)
used = [0]*(n)

f(0)
print(mn)