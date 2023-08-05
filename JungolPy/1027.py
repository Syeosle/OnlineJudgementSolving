def f(d):
    global n
    for i in range(2, d//2+1):
        if arr[d-2*i:d-i] == arr[d-i:d]: return 0
    if d == n: return 1
    for i in asdf:
        arr[d]=i
        if arr[d] == arr[d-1]: continue
        if f(d+1) == 1: return 1


n = int(input())
arr, asdf = [0]*80, [1, 2, 3]
f(0)
for i in range(n):
    print(arr[i], end='')
