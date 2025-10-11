#17m
# Lv2 58%
from collections import defaultdict
def solution(record):
    answer = []
    dic = defaultdict()
    n = len(record)
    result = []
    for i in range(n):
        rec = record[i].split(" ")

        if rec[0]!="Change":
            result.append([rec[1], rec[0]])
        
        if rec[0] in ['Enter', 'Change']:
            dic[rec[1]]=rec[2]
        
    for r in result:
        if r[1]=="Enter":
            msg = dic[r[0]]+"님이 들어왔습니다."
        else:
            msg = dic[r[0]]+"님이 나갔습니다."
        answer.append(msg)
    
    return answer