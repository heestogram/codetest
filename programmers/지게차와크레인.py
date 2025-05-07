from collections import deque

def solution(storage, requests):
    answer = 0
    n = len(storage)
    m = len(storage[0])
    visited = [[False]*m for _ in range(n)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    def bfs(x,y):
        queue = deque()
        queue.append((x,y))
        visited2[x][y]=True
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if 0>nx or nx>n-1 or 0>ny or ny>m-1:
                    return True
                elif visited[nx][ny] and not visited2[nx][ny]:
                    queue.append((nx,ny))
                    visited2[nx][ny]=True
        return False

    for req in requests:

        remove=[]
        for i in range(n):
            for j in range(m):
                if storage[i][j]==req[0] and not visited[i][j]:
                    print(req[0], i,j)
                    if len(req)==1:
                        visited2=[[False]*m for _ in range(n)]
                        if bfs(i,j):

                            remove.append((i,j))
                    else:

                        remove.append((i,j))
                        
        for re in remove:
            visited[re[0]][re[1]]=True

    for vi in visited:
        answer+=sum(vi)

    return n*m-answer