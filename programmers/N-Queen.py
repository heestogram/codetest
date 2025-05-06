def solution(n):

    map = [0]*n
    answer = dfs(map, 0, n)
    return answer

def dfs(map, row, n):
    count = 0
    if row == n:
        return 1
    
    for col in range(n):
        map[row]=col
        
        for i in range(row):
            if map[i]==col:
                break
            if abs(map[i]-col)==row-i:
                break
        else:
            count += dfs(map, row+1, n)
    return count