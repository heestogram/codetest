# 44m
# level 2 62%
from collections import deque

def solution(msg):
    answer=[]
    dic = {}
    for i in range(26):
        dic[chr(i+65)]=i+1
    last_num = 26
    
    queue = deque()
    for m in range(len(msg)):
        queue.append(msg[m])
        
    while queue:
        cur = 0
        cur_word = ""
        while True:
            cur_word+=queue[cur]
            if cur+1>=len(queue):
                answer.append(dic[cur_word])
                return answer
            if cur_word+queue[cur+1] in dic:
                cur+=1
            else:
                break
        answer.append(dic[cur_word])
        last_num+=1
        dic[cur_word+queue[cur+1]]=last_num
        for _ in range(cur+1):
            queue.popleft()
            
    return 0