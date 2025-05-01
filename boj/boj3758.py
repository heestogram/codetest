import sys
from collections import defaultdict

t = int(input())


for i in range(t):
    n,k,id,m = map(int,input().split())
    info = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

    score = [[0]*k for _ in range(n)]
    submit = [0]*n
    time = [0]*n

    count = 0
    for item in info:
        count+=1
        if item[2]>score[item[0]-1][item[1]-1]:
            score[item[0]-1][item[1]-1] = item[2]
        submit[item[0]-1]+=1
        time[item[0]-1]=count

    final = {}
    for i in range(n):
        final[i] = (sum(score[i]),submit[i],time[i])

    answer = list(final.keys())

    answer.sort(key = lambda x: (-final[x][0], final[x][1], final[x][2]))

    print(answer.index(id-1)+1)

