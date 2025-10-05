# 30m
# lveel 2 61%
 
from collections import deque

def solution(x, y, n):
    if x==y:
        return 0
    queue = deque([(x,0)])
    visited = set()
    while queue:
        x, depth = queue.popleft()
        
        for cur in (x+n, x*2, x*3):
            if cur > y:
                continue
            if cur == y:
                return depth+1

            if cur not in visited:
                visited.add(cur)
                queue.append((cur, depth+1))

    return -1