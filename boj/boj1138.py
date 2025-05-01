n = int(input())

info = list(map(int,input().split()))


line = [False]*n

for i in range(n):
    count=-1
    for l in range(n):
        if not line[l]:
            count+=1
        if count==info[i]:
            line[l]=i+1
            break

print(*line)