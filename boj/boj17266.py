import math

n = int(input())
m = int(input())
x = list(map(int, input().split()))

max_gap = x[0]  

for i in range(1, m):
    max_gap = max(max_gap, math.ceil((x[i] - x[i-1]) / 2))

max_gap = max(max_gap, n - x[-1])  

print(max_gap)
