# 22m
def solution(n):
    ans = 0
    if n==1:
        return 1 
    
    while n >1:
        if n%2!=0:
            n-=1
            ans+=1
        else:
            n=n/2
    
    return ans+1