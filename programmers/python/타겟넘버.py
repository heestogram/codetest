

def solution(numbers, target):
    answer = 0
    def dfs(num, cnt):
        nonlocal answer
        if cnt==len(numbers):
            if num==target:
                answer += 1
            return

        dfs(num+numbers[cnt], cnt+1) 
        dfs(num-numbers[cnt], cnt+1)
    
    dfs(0, 0)
        
    return answer