# 40m Lv3 49%
from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    
    adj = [[] for _ in range(n+1)]
    for road in roads:
        adj[road[0]].append(road[1])
        adj[road[1]].append(road[0])
        
    time = [[] for _ in range(n+1)]
    time[destination]=0

    queue = deque([destination])
    while queue:
        cur = queue.popleft()
        for nxt in adj[cur]:
            if not time[nxt]:
                time[nxt] = time[cur]+1
                queue.append(nxt)
    
    for src in sources:
        if not time[src]:
            answer.append(-1)
        elif src == destination:
            answer.append(0)
        else:
            answer.append(time[src])

    return answer