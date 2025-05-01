import sys
from collections import deque

m, n = map(int, input().split())
box = []


count = 0
for i in range(n):
    box.append(list(map(int, sys.stdin.readline().split())))
    count += box[i].count(0)

if count ==0:
    print(0)
    exit()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

def bfs(queue):
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx>=n or ny>=m or nx<0 or ny<0:
                continue
            if box[nx][ny]==0:
                queue.append((nx,ny))
                box[nx][ny]=box[x][y]+1
    return count

for i in range(m):
    for j in range(n):
        if box[j][i]==1:
            queue.append((j,i))

bfs(queue)

count=0
result=0

for i in box:
    count+= i.count(0)
    if count>0:
        print(-1)
        exit()

print(max(map(max,box))-1)

