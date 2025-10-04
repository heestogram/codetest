#level2 61%
# 못 풂... 40m 정도 소요

def solution(order):
    answer = 0
    stack = []
    cur=0
    idx=0
    n = len(order)
    while cur<=n:
        stack.append(cur)
        while stack and stack[-1]==order[idx]:
            stack.pop()
            idx+=1
            if idx==n:
                return n
        cur+=1
        
    return idx