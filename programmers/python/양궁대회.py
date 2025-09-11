from itertools import combinations_with_replacement
def solution(n, info):
    length=11
    result=[]
    for combi in combinations_with_replacement(range(length), n):
        lion=0
        lion_info=[0]*11
        for c in combi:
            lion_info[10-c]+=1
            
        for i in range(length):
            if lion_info[i]>info[i]:
                lion+=(10-i)
            elif lion_info[i]<=info[i] and info[i]>0:
                lion-=(10-i)
        result.append((lion,lion_info))
        
    result.sort(key=lambda x: -x[0])
    if result[0][0]<=0:
        return [-1]
    return result[0][1]