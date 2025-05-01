import sys
n = int(input())

present = list(map(int, sys.stdin.readline().rstrip()))
target = list(map(int, sys.stdin.readline().rstrip()))


def switch(pre, tar):
    count=0
    pre_ = pre[:]
    for i in range(1,n):
        if pre_[i-1]!=tar[i-1]:
            count += 1
            for j in range(i-1,i+2):
                if j < n:
                    pre_[j] = 1-pre_[j]

    if pre_ == tar:
        return(count)
    else:
        return(-1)
        
result1 = switch(present, target)

present_switched = present[:]
present_switched[0] = 1-present_switched[0]
present_switched[1] = 1-present_switched[1]
result2 = switch(present_switched, target)

if result1 == -1 and result2 == -1:
    print(-1)
elif result1 == -1:
    print(result2 + 1)
elif result2 == -1:
    print(result1)
else:
    print(min(result1, result2 + 1))