n = int(input())

req = list(map(int, input().split()))
budget = int(input())

left = 1
right = max(req)
answer=0

while left<=right:
    mid = (left+right)//2
    total = 0
    for r in req:
        if r>mid:
            total+=mid
        else:
            total+=r
    
    if total <= budget:
        answer = mid
        left = mid+1
    else:
        right = mid-1

print(answer)
