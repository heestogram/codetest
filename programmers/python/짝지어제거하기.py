#2:01
# 30m Lv2 75% 
# 논리는 맞는데 시간초과로 틀림.
from collections import deque
def solution(s):
    stack = []
    
    for cur in s:
        if stack and stack[-1]==cur:
            stack.pop()
        else:
            stack.append(cur)
    if stack:
        return 0
    else:
        return 1