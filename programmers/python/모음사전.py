def solution(word):
    answer = 0
    order = []
    mo = ["A","E","I","O","U"]
    def dfs(w):
        if len(w)==5:
            return
        for m in mo:
            new_word = w + m
            order.append(new_word)
            
            dfs(new_word)
    
    dfs("")
    answer = order.index(word)+1
    return answer