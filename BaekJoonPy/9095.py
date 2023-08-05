import sys


mem = [1, 1, 2, 4]


def num_123(n):
    if len(mem) > n: return mem[n]
    for i in range(len(mem), n + 1):
        mem.append(mem[i-3] + mem[i-2] + mem[i-1])
    return mem[n]


for _ in range(int(input())):
    n = int(sys.stdin.readline())
    print(num_123(n))