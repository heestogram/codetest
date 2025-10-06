# Lv2 64% 60m
# 거의 다 풀었는데..
def solution(dirs):
    y_visited = [[False]*11 for i in range(10)]
    x_visited = [[False]*10 for i in range(11)]

    answer = 0
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    direct = {"D":0, "U":1, "L":2, "R":3}
    x,y=5,5
    for d in dirs:
        cur_d = direct[d]
        x = x+dx[cur_d]
        y = y+dy[cur_d]
        if x<0 or x>10 or y<0 or y>10:
            x = x-dx[cur_d]
            y = y-dy[cur_d]
            continue
        if cur_d==1:
            y_visited[y-1][x]=True
        elif cur_d==0:
            y_visited[y][x]=True
        elif cur_d==2:
            x_visited[y][x]=True
        elif cur_d==3:
            x_visited[y][x-1]=True

    answer=0
    for i in y_visited:
        for j in i:
            answer+=j
    for i in x_visited:
        for j in i:
            answer+=j
    return answer