# 6:56
# Lv3 50%
from collections import deque
from collections import defaultdict
import heapq
def solution(stones, k):
    answer = 0
    order = []
    dic = defaultdict(list)
    
    for i, j in enumerate(stones):
        dic[j].append(i)
        
    for i in list(dic.keys()):
        order.append((i,dic[i]))
    zero = []
    order.sort(key=lambda x: x[0])
    queue = deque(order)
    
    cnt = 0
    while queue:
        cnt_hubo, delete = queue.popleft()
        zero+=delete
        zero.sort()
        empty=0
        for i in range(len(zero)-1):
            if zero[i] == zero[i+1]-1:
                empty+=1
            else:
                empty=0
            if empty==k-1:
                return cnt_hubo

        
    
    return cnt_hubo