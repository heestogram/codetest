import sys
from collections import deque

m,n,h = map(int, input().split())

graph = []
for i in range(h):
    box = []
    for j in range(n):
        box.append(list(map(int,sys.stdin.readline().split())))
    graph.append(box)

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs():
    while queue:
        z,y,x = queue.popleft()

        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]

            if nx>=m or ny>=n or nz>=h or nx<0 or ny<0 or nz<0:
                continue
            if graph[nz][ny][nx]==0:
                graph[nz][ny][nx]=graph[z][y][x]+1
                queue.append((nz,ny,nx))



queue = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if graph[i][j][k]==1:
                queue.append((i,j,k))

bfs()

result=0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit()
        result = max(result,max(j))

print(result-1)