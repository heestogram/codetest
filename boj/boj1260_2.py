import sys
from collections import deque
input = sys.stdin.readline

n,m,v = map(int,input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()

order = []
visited = [False]*n
def dfs(graph, v, order, visited):
    visited[v-1]=True
    order.append(v)
    for i in graph[v]:
        if not visited[i-1]:
            dfs(graph, i, order, visited)

dfs(graph, v, order, visited)
print(*order)

order = []
visited = [False]*n
def bfs(graph, v, order, visited):
    queue = deque()
    queue.append(v)
    visited[v-1]=True
    while queue:
        i = queue.popleft()
        order.append(i)
        for j in graph[i]:
            if not visited[j-1]:
                queue.append(j)
                visited[j-1]=True

bfs(graph, v, order, visited)
print(*order)
