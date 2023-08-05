import sys
def ipt(): return map(int,sys.stdin.readline().split())
n,cap=ipt();m=int(input());r,pik,cnt,capAtVil=[0]*m,[],0,[cap]*n
for i in range(m):r[i]=list(ipt())
r.sort(key=lambda x:x[1])
for i in r:
    mn=cap
    for j in range(i[0], i[1]):
        if (capAtVil[j]<mn): mn=capAtVil[j]
    tmp = min(mn, i[2])
    if tmp!=0:
        pik.append(i[:2]+[tmp])
        for j in range(i[0], i[1]): capAtVil[j]-=tmp
        cnt+=tmp
print(cnt)