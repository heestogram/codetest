# 18m
# Lv1 54%
def solution(survey, choices):
    dic = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    answer = ''
    for i in range(len(survey)):
        dic[survey[i][0]] += 4-choices[i]
    
    for typ in ["RT","CF","JM","AN"]:
        score = dic[typ[0]]-dic[typ[1]]
        if score>=0:
            answer += typ[0]
        else:
            answer += typ[1]
        
    return answer