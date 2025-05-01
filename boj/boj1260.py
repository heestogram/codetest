import sys
from collections import deque
from collections import defaultdict

input = sys.stdin.readline

n,m,v = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    v1,v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


for i in range(1,n+1):
    g = graph[i]
    g.sort()
    graph[i]=g
print(graph)

visited = [False]*n
dfs_order = []
def dfs(graph, visited, v, dfs_order):
    visited[v-1]=True
    dfs_order.append(v)
    for i in graph[v]:
        if not visited[i-1]:
            dfs(graph, visited, i, dfs_order)

dfs(graph, visited, v, dfs_order)
print(*dfs_order)


visited = [False]*n
bfs_order = []
def bfs(graph, visited, v, bfs_order):
    visited[v-1]=True
    queue = deque()
    queue.append(v)

    while queue:
        i = queue.popleft()
        bfs_order.append(i)
        for j in graph[i]:
            if not visited[j-1]:
                queue.append(j)
                visited[j-1]=True


bfs(graph, visited, v, bfs_order)
print(*bfs_order)

