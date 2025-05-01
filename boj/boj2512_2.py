import sys

input = sys.stdin.readline

n = int(input())

request = list(map(int, input().split()))

m = int(input())
maxim=0

left = 1
right = max(request)

while left<=right:
    mid = (left+right)//2
    total = 0
    for i in request:
        if i > mid:
            total += mid
        else:
            total += i

    if total <= m:
        maxim = mid
        left = mid+1
    else:
        right = mid-1


print(maxim)