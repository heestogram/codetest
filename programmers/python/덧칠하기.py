#44m
#Lv1 65%
from collections import deque
def solution(n, m, section):
    queue = deque(section)
    right=section[0]+m-1
    trial = 1
    for i in range(1,len(section)):
        if right >= section[-1]:
            return trial
        while True:
            if queue[0]>right:
                break
            queue.popleft()
            
            
        right=queue[0]+m-1
        trial+=1
    
    return trial