

from collections import deque

def solution(maps):
    queue=deque()
    answer = 0
    n=len(maps)
    m=len(maps[0])
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    def bfs():
        queue.append((0,0))
        while queue:
            x,y = queue.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<=n-1 and 0<=ny<=m-1 and maps[nx][ny]==1:
                    maps[nx][ny] = maps[x][y]+1
                    queue.append((nx,ny))


    bfs()
    if maps[n-1][m-1]==1:
        answer = -1
    else:
        answer = maps[n-1][m-1]

    return answer