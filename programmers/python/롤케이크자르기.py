
# level 2 65%
# 못 풂 ㅜ 30분정도

from collections import Counter

def solution(topping):
    right = Counter(topping)
    left = set()
    right_cnt = len(right)
    left_cnt = 0
    answer=0
    for top in topping:
        right[top]-=1
        if right[top]==0:
            right_cnt-=1
            del right[top]
        if top not in left:
            left.add(top)
            left_cnt+=1

        if left_cnt==right_cnt:
            answer+=1
    

    return answer