# 20m
# Lv3 56%
from collections import defaultdict

def solution(genres, plays):
    dic = defaultdict(list)
    answer=[]
    def ver_sum(mat):
        summ=0
        for i in range(len(mat)):
            summ+=mat[i][0]
        return summ
    
    for i in range(len(genres)):
        dic[genres[i]].append((plays[i],i))
        
    sort_gen = list(set(genres))
    sort_gen.sort(key=lambda x: -ver_sum(dic[x]))
    
    for gen in sort_gen:
        cur_list = dic[gen]
        cur_list.sort(key=lambda x: (-x[0],x[1]))
        answer.append(cur_list[0][1])
        if len(cur_list)>=2:
            answer.append(cur_list[1][1])
        

    return answer