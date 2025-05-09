
from itertools import combinations
from collections import defaultdict
def solution(orders, course):
    dic = defaultdict(int)
    answer = []
    for c in course:
        for order in orders:
            if len(order)<c:
                pass
            for i in combinations(order,c):
                menu = ""
                for k in i:
                    menu+=k
                menu = ''.join(sorted(menu))
                dic[menu]+=1
    result=[]
    for d in dic:
        if dic[d]>=2:
            result.append(d)
    result.sort(key=lambda x: (len(x),-dic[x]))

    
    li=[[]for _ in range(10)]
    for r in result:
        idx=len(r)-1
        li[idx].append(r)
        
    for l in li:
        if l:
            answer.append(l[0])
            for k in range(1,len(l)):
                if dic[l[k]]==dic[l[0]]:
                    answer.append(l[k])
                else:
                    break
    answer.sort()
    return answer