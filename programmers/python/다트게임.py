# 20m
# Lv1 60%

from collections import deque
def solution(dartResult):
    queue = deque()
    for r in dartResult:
        queue.append(r)
    bonus = {"S":1, "D":2, "T":3}
    answer = 0
    temp = []
    idx = 0
    while queue:
        if queue[0]=="1" and queue[1]=="0":
            queue.popleft()
            queue.popleft()
            num=10
        else:
            num = queue.popleft()
        b = queue.popleft()
        temp.append(int(num)**bonus[b])
        if not queue:
            break
        if queue[0]=="*":
            queue.popleft()
            if idx == 0:
                temp[0]*=2
            else:
                temp[idx]*=2
                temp[idx-1]*=2
        elif queue[0]=="#":
            queue.popleft()
            temp[idx]*=(-1)
                
        idx+=1
    return sum(temp)