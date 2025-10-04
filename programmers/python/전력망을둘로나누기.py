import copy
def solution(n, wires):
    v = [[] for _ in range(n+1)]
    for w in wires:
        v[w[0]].append(w[1])
        v[w[1]].append(w[0])
        
    answer=100
    for i in range(n-1):

        visited = [False]*(n+1)
        v1, v2 = wires[i]
        visited[v2] = True
        
        def dfs(start):
            cnt = 1
            visited[start]=True
            for i in v[start]:
                if not visited[i]:
                    visited[i]=True
                    cnt+=dfs(i)
            return cnt

        diff = abs(dfs(v1)-dfs(v2))
        answer = min(diff, answer)

    return answer