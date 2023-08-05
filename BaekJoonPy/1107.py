from time import time as tt

goal = int(input())
input()
banned = list(map(int, input().split()))

stt = tt()

def movable(n):
    if n == 0:
        return 0 not in banned


    for i in banned:
        tmp = n
        while tmp > 0:
            if tmp % 10 == i: return False
            tmp //= 10
    return True


def digit(n):
    if n == 0: return 1
    cnt = 0
    while n > 0:
        cnt, n = cnt + 1, n//10
    return cnt


under_near = 100 if goal >= 100 else -1
upper_near = 100 if goal <= 100 else -1

for i in range(goal, -1, -1):
    if movable(i):
        under_near = i
        break

for i in range(goal, 500001):
    if movable(i):
        upper_near = i
        break



print(tt() - stt)
