from collections import deque
def solution(prices):
    answer=[]
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        cnt=0
        for after in queue:
            cnt+=1
            if after<price:
                break
        answer.append(cnt)
        
    return answer