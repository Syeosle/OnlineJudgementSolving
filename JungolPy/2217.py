def cov(str1, str2):
    for i in range(min(len(str1), len(str2)), 0, -1):
        if str1[-i:]==str2[:i]: return i
    return 0

def tskfull():
    for i in dnas:
        if i not in tsk: return False
    return True


mn = 362880
n = int(input())
dnas = []
for _ in range(n):
    dnas.append(input())

tsk = []


def f():
    if tskfull():
        global mn
        cnt = 0
        for i in range(len(tsk)-1):
            cnt += len(tsk[i]) - cov(tsk[i], tsk[i+1])
        cnt += len(tsk[-1])
        if cnt < mn: mn = cnt
        return
    flag = True
    for i in range(n):
        if dnas[i] not in tsk:
            tsk.append(dnas[i])
            f()
            tsk.pop()
            flag = False
    if flag: f()

f()

print(mn)