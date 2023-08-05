import sys
def ipt(): return map(int, sys.stdin.readline().split())
n,q=ipt(); logs,k=[0]*n,0
for i in range(n): logs[i]=list(ipt())[:-1]+[i, 0]
logs.sort()
for i in range(n):
    if logs[i][3]==0: k+=1;logs[i][3]=k
    for j in range(i+1,len(logs)):
        if logs[j][0]>logs[i][1]: break
        logs[j][3]=k
logs.sort(key=lambda x:x[2])
for _ in [0]*q:
    a,b=ipt()
    if logs[a-1][3]==logs[b-1][3]: print(1)
    else: print(0)