import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for i in range(n)]

dp = [[[0,0,0] for _ in range(m)]]+[[[float('inf')]*3 for _ in range(m)]for _ in range(n)]

for i in range(1,n+1):
    for j in range(m):
        if j <m-1:
            dp[i][j][0] = min(dp[i-1][j+1][1], dp[i-1][j+1][2])+graph[i-1][j]
        if 0<j:
            dp[i][j][2] = min(dp[i-1][j-1][0], dp[i-1][j-1][1])+graph[i-1][j]
        dp[i][j][1] = min(dp[i-1][j][0], dp[i-1][j][2])+graph[i-1][j]


minim = float('inf')
for i in dp[n]:
    cur = min(i)
    minim = min(cur, minim)

print(minim)