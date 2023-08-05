import sys
def ipt():return sys.stdin.readline()
w,a,b,r,sum,cnt=int(ipt()),list(map(int,(ipt().split()))),[500,100,50,10,5,1],[0]*6,0,0
for i in range(5,0,-1):
    r[i] = w % b[i - 1] // b[i]
    nxt = r[i] + b[i - 1] // b[i]
    while(nxt<=a[i] and nxt*b[i]<=w):
        r[i] = nxt
        nxt = r[i] + b[i - 1] // b[i]
    sum+=r[i]*b[i]
    w-=r[i]*b[i]
    cnt+=r[i]

r[0] = w//b[0]
cnt += r[0]

print(cnt)
for i in r:
    print(i, end=' ')