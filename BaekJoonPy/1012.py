import sys
def ipt():return sys.stdin.readline().rstrip()


g = [[[0, 0] for _ in [0]*52] for _ in [0]*52]
cds = []
qu = []


def bc(cd): return g[cd[0]][cd[1]][0]


def sc(cd, x=0):
    if x==0: return g[cd[0]][cd[1]][1]
    g[cd[0]][cd[1]][1] = x


for _ in [0]*int(ipt()):
    m, n, k = map(int, ipt().split())
    for _ in [0]*k:
        x, y = map(int, ipt().split())
        cds.append([x+1, y+1])
        g[x+1][y+1][0] = 1

    cnt = 0

    for cd in cds:
        if sc(cd) == 1: continue
        qu.append(cd)
        while (len(qu) != 0):
            if bc(qu[0]) == 0 or sc(qu[0]) == 1: qu = qu[1:]
            else:
                sc(qu[0], 1)
                qu.extend([[qu[0][0]-1, qu[0][1]], [qu[0][0]+1, qu[0][1]],
                           [qu[0][0], qu[0][1]-1], [qu[0][0], qu[0][1]+1]])
                qu = qu[1:]
        cnt += 1

    print(cnt)
    cds = []
    g = [[[0, 0] for _ in [0] * 52] for _ in [0] * 52]