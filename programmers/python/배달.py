# 1h
# Lv2 못 풂 52%
import heapq

def solution(N, road, K):
    answer = 0
    time = [10000]*N
    
    adj = [[] for _ in range(N+1)]
    for r in road:
        adj[r[0]].append((r[1],r[2]))
        adj[r[1]].append((r[0],r[2]))

    dist = [10**15] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]  # (현재거리, 노드)

    while pq:
        t, loc = heapq.heappop(pq)
        if t > dist[loc]:
            continue
        for v, w in adj[loc]:
            nd = t+w
            if nd < dist[v]:
                dist[v]=nd
                heapq.heappush(pq, (nd,v))


    
    return sum(d<=K for d in dist[1:])