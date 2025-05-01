import sys

n,m = map(int, sys.stdin.readline().split())

a=[]
b=[]

for i in range(n):
    a.append(list(map(int, sys.stdin.readline().rstrip())))
for j in range(n):
    b.append(list(map(int, sys.stdin.readline().rstrip())))


def change(r, c, mat):
    for i in range(r, r+3):
        for j in range(c, c+3):
            if mat[i][j]==0:
                mat[i][j]=1
            else:
                mat[i][j]=0   
    

count = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j]!=b[i][j]:
            change(i, j, a)
            count += 1

if a!=b:
    print(-1)
else:
    print(count)

