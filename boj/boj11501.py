import sys
input =sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    prices = list(map(int,input().split()))
    margin = 0
    now = prices[-1]
    for i in range(n-1,0,-1):
        if now>prices[i-1]:
            margin += (now-prices[i-1])
        else:
            now = prices[i-1]
    print(margin)