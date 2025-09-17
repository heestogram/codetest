def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0

    def dfs(energy, cnt):
        nonlocal answer
        answer = max(answer, cnt)

        for i in range(n):
            need, cost = dungeons[i]
            if not visited[i] and energy >= need:
                visited[i] = True       
                dfs(energy - cost, cnt + 1)   
                visited[i] = False             

    dfs(k, 0)
    return answer