n,a,s=input(),sorted(list(map(int,input().split()))),0
for i in a:
    if s+1<i: break
    s+=i
print(s+1)