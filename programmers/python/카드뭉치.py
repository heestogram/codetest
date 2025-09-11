from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    
    for g in goal:
        if queue1 and g==queue1[0]:
            queue1.popleft()
        elif queue2 and g==queue2[0]:
            queue2.popleft()
        else:
            return 'No'
        
    
    return 'Yes'