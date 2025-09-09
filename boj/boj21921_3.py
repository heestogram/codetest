n, x = map(int, input().split())

visit = list(map(int,input().split()))

cur = sum(visit[0:x])
maxim = cur
cnt=0
for i in range(x,n):
    cur -= visit[i-x]
    cur += visit[i]
    if cur > maxim:
        maxim = cur
        cnt = 1
    elif cur == maxim:
        cnt += 1

if maxim==0:
    print("SAD")
else:
    print(maxim)
    print(cnt)