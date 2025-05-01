import sys

n = int(input())

dung = []
ranks = []

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    dung.append((x,y))

for me in dung:
    rank = 1
    for comp in dung:
        if me[0]<comp[0] and me[1]<comp[1]:
            rank += 1
    ranks.append(rank)

for rank in ranks:
    print(rank, end=" ")