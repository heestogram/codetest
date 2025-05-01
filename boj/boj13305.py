import sys
n = int(input())

dist = list(map(int, sys.stdin.readline().split()))
price = list(map(int, sys.stdin.readline().split()))

min_price = price[0]
cost = 0

for i in range(n-1):
    if price[i]<min_price:
        min_price = price[i]
    cost += min_price*dist[i]

print(cost)