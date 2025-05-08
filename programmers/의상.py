from collections import defaultdict
def solution(clothes):
    clo_cnt=defaultdict(int)
    answer = 1
    for clo in clothes:
        clo_cnt[clo[1]]+=1
        
    for item in clo_cnt:
        answer= answer*(clo_cnt[item]+1)
    
    return answer-1