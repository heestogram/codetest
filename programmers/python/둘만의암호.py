# 19m
# Lv1 60%
def solution(s, skip, index):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    stack = []
    answer=""
    for alp in alpha:
        stack.append(alp)
        
    for word in s:
        idx=index
        cur = stack.index(word)
        while idx>0:
            cur += 1
            if cur>25:
                cur = 0
            if stack[cur] in skip:
                continue
            idx-=1
        answer += stack[cur]
    return answer