# 40m
# lv3 62%
from collections import deque
def solution(begin, target, words):
    answer = 0
    words = [begin]+words
    if target in words:
        final = words.index(target)
    else:
        return 0
    n = len(words)
    word_len = len(words[0])
    diff = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if j!=i:
                for k in range(word_len):
                    if words[i][k]!=words[j][k]:
                        diff[i][j]+=1
    v = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if diff[i][j]==1:
                v[i].append(j)
    print(words)
    
    visited = [False]*n
    depth = 0
    result = []
    
    queue = deque([(0,0)])
    while queue:
        cur, depth = queue.popleft()
        visited[cur]=True
        if cur == final:
            return depth
        for i in v[cur]:
            if not visited[i]:
                visited[i]=True
                queue.append((i,depth+1))
                
    
    return result