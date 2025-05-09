import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            x,y=i,j
        elif graph[i][j]==1:
            graph[i][j]=-1

dx = [0,0,1,-1]
dy = [1,-1,0,0]


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y]=0

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==-1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))

bfs(x,y)

for i in range(n):
    for j in range(m):
        print(graph[i][j], end=' ')
    print('')

    
