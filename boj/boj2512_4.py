import sys
input = sys.stdin.readline

n = int(input())

budget = list(map(int, input().split()))

m = int(input())

if sum(budget)<=m:
    print(max(budget))
    exit()

left = 1
right = max(budget)
answer = 0

while left<=right:
    mid = (left+right)//2
    total = 0
    for b in budget:
        if b>mid:
            total+=mid
        else:
            total+=b
    if total<=m:
        answer = mid
        left = mid+1 # 현재 mid값으로는 최적이 아니므로 +1을 함.
    else:
        right = mid-1 # 현재 mid값으로는 최적이 아니므로 -1을 함.


print(answer)
