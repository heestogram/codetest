import sys
from collections import deque

n = int(input())

graph = []

for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# def bfs(x,y):
#     queue = deque()
#     queue.append((x,y))
#     graph[x][y]=0
#     count=1

#     while queue:
#         x,y = queue.popleft()
#         for i in range(4):
#             nx, ny = x+dx[i], y+dy[i]
#             if 0<=nx<n and 0<=ny<n and graph[nx][ny]==1:
#                 graph[nx][ny]=0
#                 queue.append((nx,ny))
#                 count+=1
#     return count

# result = []

# for i in range(n):
#     for j in range(n):
#         if graph[i][j]==1:
#             result.append(bfs(i,j))

# result.sort()
# print(len(result))
# for item in result:
#     print(item)

def dfs(x,y):
    global count
    if x<0 or x>=n or y<0 or y>=n:
        return
    if graph[x][y]==1:
        graph[x][y]=0
        count+=1
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            dfs(nx,ny)

result=[]
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            count=0
            dfs(i,j)
            result.append(count)

result.sort()
print(len(result))
for item in result:
    print(item)