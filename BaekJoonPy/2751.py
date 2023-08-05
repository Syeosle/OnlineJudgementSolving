import sys
L,i,x=[],0,int(sys.stdin.readline().rstrip())
while(i<x):L.append(int(sys.stdin.readline().rstrip()));i+=1
L.sort()
for i in L:print(i)