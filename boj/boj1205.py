import sys
n, newscore, p = map(int, input().split())

if n>0: 
    score = list(map(int, sys.stdin.readline().split()))
else:
    print(1)
    exit()

score.append(newscore)

score.sort(reverse=True)

rank = score.index(newscore)+1

if rank > p:  
    print(-1)
elif n==p and newscore==score[-1]:
    print(-1)
else:
    print(rank)