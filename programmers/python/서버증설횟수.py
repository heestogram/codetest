# 28m
from collections import deque
def solution(players, m, k):
    # 서버 증설 때마다 큐에 5씩 넣고 한 시간 지날 때마다 -1로 차감.
    # queue[0]가 0이면 leftpop. 0 아닌 애까지 쭉 leftpop. queue도 존재한다는 조건 걸어야 함.
    # while True:
    # if queue and queue[0]==0:
        # queue.popleft()
    # else:
        # break
    answer = 0
    queue = deque()
    
    for i in range(24):
        cur = players[i]
        req = cur//m
        if req > len(queue):
            for t in range(req-len(queue)):
                answer+=1
                queue.append(k) 

        for j in range(len(queue)):
            queue[j]-=1
        ###
        # print("---")
        # print("time",i,"cur", cur, "req", req)
        # print("queue")
        # for w in range(len(queue)):
        #     print(queue[w])
        ###
        while True:
            if queue and queue[0]==0:
                queue.popleft()
            else:
                break
        # print("after delete")
        # for l in range(len(queue)):
        #     print(queue[l])
    
    return answer