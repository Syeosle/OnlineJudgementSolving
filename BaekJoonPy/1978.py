prime = [2, 3]
cnt = 0
def isprime(x):
    if x == 1: return False
    tmp = x ** 0.5
    for i in prime:
        if i > tmp: break
        if x % i == 0: return False
    return True

dmp = input()
del dmp
L = list(map(int, input().split()))
L.sort(reverse=True)

tmp = L[0] ** 0.5

for i in range(5, int(tmp) + 1):
    if isprime(i): prime.append(i)

for i in L:
    if i in prime: cnt += 1
    elif isprime(i): cnt += 1

print(cnt)