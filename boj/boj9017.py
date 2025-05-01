import sys
from collections import defaultdict

t = int(input())

for j in range(t):
    n = int(input())

    table = defaultdict(int)
    rank = defaultdict(list)

    player = list(map(int, sys.stdin.readline().split()))
    
    for i in player:
        table[i]+=1

    valid = [x for x in table if table[x]<6]

    for i in valid:
        while i in player:
            player.remove(i)

    for index, team in enumerate(player):
        rank[team].append(index)

    result = list(rank.keys())

    result.sort(key = lambda x : (sum(rank[x][:4]), rank[x][4], rank[x][5]))

    print(result[0])
