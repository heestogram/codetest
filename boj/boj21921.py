# 슬라이딩 윈도우

import sys
n, x = map(int, sys.stdin.readline().split())

visit = list(map(int, sys.stdin.readline().split()))

if sum(visit)==0:
    print("SAD")
    exit()

current = sum(visit[0:x])
maxim = current
count = 1

for i in range(x,n):
    current += visit[i]
    current -= visit[i-x]
    if current>maxim:
        count = 1
        maxim = current
    elif current == maxim:
        count+=1

print(maxim)
print(count)