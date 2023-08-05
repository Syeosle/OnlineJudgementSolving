n = int(input())
opened = list(map(int, input().split()))
t = int(input())

mn, ind, cnt, tsk = 3628800, 0, 0, [0]*t

for i in range(t):
    tsk[i] = int(input())

def f():
    global mn, ind, cnt
    if cnt > mn: return
    if ind == t:
        mn = cnt
        return

    d1 = abs(tsk[ind] - opened[0])
    d2 = abs(tsk[ind] - opened[1])

    tmp, opened[0] = opened[0], tsk[ind]
    ind += 1
    cnt += d1
    f()
    ind -= 1
    cnt -= d1
    opened[0] = tmp
    tmp, opened[1] = opened[1], tsk[ind]
    ind += 1
    cnt += d2
    f()
    ind -= 1
    cnt -= d2
    opened[1] = tmp

    return


f()

print(mn)