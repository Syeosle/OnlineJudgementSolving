import sys
from collections import deque
f_in = sys.stdin.readline


def main():
    N, K = map(int, f_in().split())
    time = [0] + list(map(int, f_in().split()))
    req = [[] for _ in range(N + 1)]
    nxt = [[] for _ in range(N + 1)]

    for _ in range(K):
        fr, to = map(int, f_in().split())
        req[to].append(fr)
        nxt[fr].append(to)
    inDeg = [len(j) for j in req]

    w = int(f_in())
    q = deque()
    for i in range(1, N + 1):
        if inDeg[i] == 0: q.append(i)

    i = 0
    while i != w:
        i = q.popleft()
        for j in nxt[i]:
            inDeg[j] -= 1
            if inDeg[j] == 0: q.append(j)

        time[i] += max([0]+[time[j] for j in req[i]])

    print(time[w])


for _ in range(int(f_in())): main()
