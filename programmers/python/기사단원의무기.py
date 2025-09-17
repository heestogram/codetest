# 25m 00s

import math
def solution(number, limit, power):
    answer = 0
    yaksu = [0]*(number+1)
    
    for num in range(1,number+1):
        for i in range(num,number+1,num):
            yaksu[i]+=1
            
    for p in yaksu:
        if p<=limit:
            answer+=p
        else:
            answer+=power
    return answer