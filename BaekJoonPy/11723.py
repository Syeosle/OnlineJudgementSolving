import sys
s = [0]*20
i = int(input())
while(i>0):
    a = sys.stdin.readline().rstrip().split()
    if len(a) > 1: b = int(a[1])-1
    a = a[0][1]
    if a == 'd': s[b]=1
    elif a == 'e': s[b]=0
    elif a == 'h': print(s[b])
    elif a == 'o':
        if s[b] == 0: s[b] = 1
        else: s[b]=0
    elif a == 'l': s = [1]*20
    elif a == 'm': s = [0]*20
    i -= 1