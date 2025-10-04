# 38m
# lv3 62%
def solution(n, works):
    works.sort(reverse=True)
    idx = 0
    maxim = len(works)
    while n>0:
        if idx+1!=maxim and works[idx]<works[idx+1]:
            idx+=1
        else:
            idx=0
        works[idx]-=1
        n-=1
        
    if sum(works)<=0:
        return 0
    answer=0
    for w in works:
        answer+=w**2
    
        
    return answer