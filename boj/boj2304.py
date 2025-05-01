import sys
input = sys.stdin.readline

n = int(input())

pillar = [list(map(int,input().split())) for _ in range(n)]
pillar.sort(key = lambda x: x[0])

maxim = max(list(map(lambda x: x[1], pillar)))
maxidx = list(map(lambda x: x[1], pillar)).index(maxim)

maxidx=[]
for i in range(n):
    if list(map(lambda x: x[1], pillar))[i]==maxim:
        maxidx.append(i)

result = 0

nowh = pillar[0][1]
nowl = pillar[0][0]
for i in range(0,maxidx[0]):
    if nowh < pillar[i][1]:
        width = abs(nowl-pillar[i][0])
        result += nowh*width
        nowl = pillar[i][0]
        nowh = pillar[i][1]

result+=abs(nowl-pillar[maxidx[0]][0])*nowh

nowh = pillar[-1][1]
nowl = pillar[-1][0]
for j in range(n-1,maxidx[-1],-1):
    if nowh < pillar[j][1]:
        width = abs(nowl-pillar[j][0])
        result += nowh*width
        nowl = pillar[j][0]
        nowh = pillar[j][1]
result+=abs(nowl-pillar[maxidx[-1]][0])*nowh

result+= maxim*(pillar[maxidx[-1]][0]-pillar[maxidx[0]][0]+1)
print(result)