import sys

n,k = map(int, input().split())

nations = []
for i in range(n):
    nation = list(map(int, sys.stdin.readline().split()))
    nations.append(nation)

for nation in nations:
    if nation[0]==k:
        target = nation
        break

rank=1
for i in range(1,4):
    tie = []
    for nation in nations:
        if nation[i]>target[i]:
            rank+=1
        if nation[i]==target[i]:
            tie.append(nation)

    nations = tie

print(rank)