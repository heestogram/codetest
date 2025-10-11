# 40m
# Lv2 69%
from collections import deque
def solution(s):
    answer = 0


    
    dic = {"(":")", "{":"}", "[":"]"}
    queue = deque()
    
    for i in s:
        queue.append(i)
    n = len(queue)
    for j in range(n):
        stack = []
        for i in range(n):
            cur = queue[i]
            if cur in ["(","{","["]:
                stack.append(cur)
            else:
                if stack:
                    cur_open = stack.pop()
                    if dic[cur_open]!=cur:
                        break
                else:
                    break
            # print(cur, stack)
            if i == n-1 and not stack:
                answer+=1
        first = queue.popleft()
        queue.append(first)
        
    return answer