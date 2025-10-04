from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        flag = False
        cur = queue.popleft()
        idx=1
        for after in queue:
            if after<cur:
                answer.append(idx)
                flag=True
                break
            idx+=1
        if not flag:
            answer.append(idx-1)
        
    return answer