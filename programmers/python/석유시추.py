from collections import deque, defaultdict
import copy
def solution(land):
    answer = 0
    n=len(land)
    m=len(land[0])
    visited = [[False]*m for _ in range(n)]
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        count=1
        visited[x][y]=True
        col=[y]
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i],y+dy[i]
                if 0<=nx<=n-1 and 0<=ny<=m-1 and land[nx][ny]==1 and not visited[nx][ny]:
                    count+=1
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    col.append(ny)
        col_set = list(set(col))
        return count, col_set
    
    answer=defaultdict(int)
    for i in range(m):
        for j in range(n):
            if land[j][i]==1 and not visited[j][i]:
                oil, col = bfs(j,i)
                for c in col:
                    answer[c]+=oil

                    
    result = list(answer.values())          
                    
    return max(result)