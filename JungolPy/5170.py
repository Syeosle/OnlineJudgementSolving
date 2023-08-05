import sys
def ipt(): return map(int, sys.stdin.readline().split())

mx, m = ipt(); mx-=1; mn = 0
ar = sorted(list(ipt()), reverse=True)

def get(x):
    sum=0
    for i in ar:
        if x<i: sum+=i-x
        else: break
    return sum

def lev1(mx, mn):
    mid = (mx+mn)//2
    if mid==mn: return ar[mx]
    a, b = get(ar[mid]), get(ar[mid-1])
    if a>=m and m>=b: return ar[mid]
    if a>=m and b>=m: return lev1(mid, mn)
    else: return lev1(mx, mid)

k = lev1(mx, mn)
if get(k)<m:
    while(get(k)<m): k-=1
    print(k)
else:
    while(get(k)>=m): k+=1
    print(k-1)