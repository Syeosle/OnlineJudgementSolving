p,p[0]=[0]*42,1
for j in range(2,42):p[j]=p[j-1]+p[j-2]
for i in [0]*int(input()):x=int(input());print(p[x],p[x+1])