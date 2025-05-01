import sys
import math

n = int(input())

request = list(map(int, sys.stdin.readline().split()))

m = int(input())

maxim = 0

left = 1
right = max(request)

while left <= right:
    mid = (left+right)//2
    total = 0

    for item in request:
        if item >= mid:
            total += mid
        else:
            total += item
    if total <= m:
        maxim = mid
        left = mid+1
    else:
        right = mid-1

print(maxim)


# total = m+1
# max = max(request)

# while total > m:
#     for i in range(n):
#         if request[i] >= max:
#             request[i] = request[i]-1
#             max = request[i]
#     total = sum(request)

# print(max)