import sys

n = int(input())

graph = []

for i in range(n):
    a = list(sys.stdin.readline().rstrip())
    graph.append(a)

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def findheart():
    for i in range(n):  
        for j in range(n):  
            if graph[i][j] == "*":
                return (i+1, j) 

def ruler(coord, direct):
    count = 0
    nx,ny = coord
    while graph[nx][ny]=="*":

        nx, ny = nx+dy[direct], ny+dx[direct]
        count+=1
        if nx>=n or ny>=n or nx==-1 or ny==-1:
            break
    return count-1, (nx-1, ny)

heart = findheart()

leftarm,_ = ruler(heart,0)
rightarm,_ = ruler(heart,1)
waist,waistcoord = ruler(heart,2)

leftleg,_ = ruler((waistcoord[0]+1,waistcoord[1]-1),2)
rightleg,_ = ruler((waistcoord[0]+1,waistcoord[1]+1),2)

x,y=heart
print(x+1, y+1)
print(leftarm, rightarm, waist, leftleg+1, rightleg+1)
