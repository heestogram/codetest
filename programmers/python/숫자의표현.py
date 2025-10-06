# 28m
# Lv2 76%
def solution(n):
    answer = 1 # 자기 자신인 경우 포함
    start = 1
    cur = start
    add = start
    while start < n/2:
        if cur == n:
            answer += 1
            start += 1
            cur = start
            add = start
        elif cur > n:
            start += 1
            cur = start
            add = start
        else:
            add+=1
            cur += add
    return answer