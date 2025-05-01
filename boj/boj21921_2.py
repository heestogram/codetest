n, x = map(int, input().split())

visit = list(map(int, input().split()))
count=1
summ = sum(visit[0:x])
max = summ

for i in range(x,n):
    summ += visit[i]
    summ -= visit[i-x]
    if summ>max:
        count=1
        max = summ
    elif summ==max:
        count+=1

if max == 0:
    print("SAD")
    exit()

print(max)
print(count)