# 1시 40분 시작
# 1시 40분 시작
def solution(n, computers):
    answer = 0
    visited = [False]*n
    
    def dfs(start):
        visited[start]=True
        for i in range(n):
            if computers[start][i]==1 and not visited[i]:
                dfs(i)
                
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer+=1
    
    return answer



# def solution(n, computers):
#     answer = 0
#     v = []
#     for i in range(n):
#         vv = []
#         for j in range(n):
#             if computers[i][j]==1 and i!=j:
#                 vv.append(j)
#         v.append(vv)
    
#     visited = [False]*n
    
#     def dfs(start):
#         visited[start]=True
#         for i in v[start]:
#             if not visited[i]:
#                 dfs(i)
        
    
#     for i in range(n):
#         if not visited[i]:
#             dfs(i)
#             answer+=1
#     return answer