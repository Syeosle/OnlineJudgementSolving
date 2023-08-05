import sys
def ipt(): return map(int, sys.stdin.readline().split())
n=int(input());r,cnt,key,next,brkp=[],0,301,0,0
for _ in [0]*n: r.append((lambda x:[x[0]*100+x[1],x[2]*100+x[3]])(list(ipt())))
r.sort()
r+=[[1300,1300]]
if r[0][0]<302:
    for i in r:
        if i[0]>key:
            if key<brkp: cnt=0;break
            cnt+=1;key,next=next,0
            if key>1130: break
        if i[1]>next:next=i[1]
        brkp=i[0]
if key<1201:cnt=0
print(cnt)