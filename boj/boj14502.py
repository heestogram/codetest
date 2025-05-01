

### 시간초과 ###

# import sys, copy
# from collections import deque

# n, m = map(int, input().split())

# graph = []

# for i in range(n):
#     graph.append(list(map(int, sys.stdin.readline().split())))

# def makewall(count):
#     if count == 3:
#         bfs()
#         return
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j]==0:
#                 graph[i][j]=1
#                 makewall(count+1)
#                 graph[i][j]=0

# dx=[-1,1,0,0]
# dy=[0,0,-1,1]

# def bfs():
#     queue = deque()
#     copy_graph = copy.deepcopy(graph)
#     for i in range(n):
#         for j in range(m):
#             if copy_graph[i][j]==2:
#                 queue.append((i,j))
#     while queue:
#         x,y=queue.popleft()
#         for i in range(4):
#             nx = x+dx[i]
#             ny = y+dy[i]
#             if nx>=n or ny>=m or nx<0 or ny<0:
#                 continue
#             if copy_graph[nx][ny]==0:
#                 queue.append((nx,ny))
#                 copy_graph[nx][ny]=2

#     global result
#     count = 0
#     for i in range(n):
#         count+=copy_graph[i].count(0)
#     result = max(count, result)

# result=0
# makewall(0)
# print(result)


import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 벽을 세울 수 있는 모든 위치
empty_spaces = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 0]

# 바이러스 위치
viruses = [(i, j) for i in range(n) for j in range(m) if graph[i][j] == 2]

# BFS로 바이러스 퍼뜨리기
def bfs():
    queue = deque(viruses)
    visited = [[False] * m for _ in range(n)]
    temp_graph = [row[:] for row in graph]  # 그래프 복사

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and temp_graph[nx][ny] == 0:
                temp_graph[nx][ny] = 2  # 바이러스 확산
                visited[nx][ny] = True
                queue.append((nx, ny))
    
    return sum(row.count(0) for row in temp_graph)

# 모든 벽 조합에 대해 시뮬레이션
result = 0
for walls in combinations(empty_spaces, 3):
    # 벽 세우기
    for x, y in walls:
        graph[x][y] = 1

    # 바이러스 퍼뜨리고 안전 영역 계산
    result = max(result, bfs())

    # 벽 원상복구
    for x, y in walls:
        graph[x][y] = 0

print(result)
