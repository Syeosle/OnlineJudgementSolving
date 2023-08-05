def isgw(str):
    abSet = list(set(str))
    for i in abSet:
        legacy = ""
        for j in range(1, len(str)):
            if str[j-1] == i and str[j] != i:
                legacy = str[j:]
                break
        if i in legacy: return False
    return True


n = int(input())
cnt = 0
for i in range(n):
    if isgw(input()): cnt += 1
print(cnt)