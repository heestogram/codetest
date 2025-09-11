def solution(park, routes):
    answer = []
    dx = [-1,1,0,0] #N,S,W,E
    dy = [0,0,-1,1]
    dic={"N":0, "S":1, "W":2, "E":3}
    n=len(park)
    m=len(park[0])
    for i in range(n):
        for j in range(m):
            if park[i][j]=="S":
                x,y=i,j
    for com in routes:
        loc, dist = com.split(" ")
        print("---")
        print(loc, dist)
        temp_x, temp_y = x,y
        broken=False
        for dis in range(int(dist)):
            
            nx, ny = temp_x+dx[dic[loc]], temp_y+dy[dic[loc]]
            print(nx,ny)
            if 0<=nx<=n-1 and 0<=ny<=m-1 and park[nx][ny]!="X":
                temp_x,temp_y = nx,ny
            else:
                print("fail")
                broken=True
                break
        if not broken:
            x,y = x+int(dist)*dx[dic[loc]], y+int(dist)*dy[dic[loc]]

    answer.append(x)
    answer.append(y)
    
    return x,y