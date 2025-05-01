import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

info = [input().split() for _ in range(n)]

result = []

for i in range(m):
    stat = int(input())
    right = len(info)
    left = 0
    while left <= right:
        mid = (left+right)//2
        if int(info[mid][1])>=stat:
            right = mid-1
            result = mid
        else:
            left = mid+1
    print(info[result][0])
