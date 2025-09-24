#10m
from itertools import combinations
def solution(nums):
    
    def sosu(n):
        for i in range(2,n//2+1):
            if n%i==0:
                return 0
        return 1
    
    answer = 0
    
    for i in combinations(nums,3):
        summ = sum(i)
        answer += sosu(summ)

    return answer