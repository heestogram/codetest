import sys, heapq

n, k = map(int, sys.stdin.readline().split())

coins = []
for i in range(n):
    coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

count = 0

for coin in coins:
    count += k//coin
    k = k%coin

print(count)