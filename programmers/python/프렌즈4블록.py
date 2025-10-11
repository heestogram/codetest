# 1h 5m
# Lv2 58%
def solution(m, n, board):
    answer = 0
    graph=[]
    for i in range(n):
        col = []
        for j in range(m):
            col.append(board[j][i])
        graph.append(col[::-1])
        
    answer=0
    while True:
        delete = [[0]*m for _ in range(n)]
        for col in range(n-1):
            if len(graph[col])<=len(graph[col+1]):
                row = len(graph[col])-1
            else:
                row = len(graph[col+1])-1
            
            while row>=1:
                # print("row", row, "col", col)
                if graph[col][row]==graph[col][row-1]==graph[col+1][row]==graph[col+1][row-1]:
                    delete[col][row]+=1
                    delete[col][row-1]+=1
                    delete[col+1][row]+=1
                    delete[col+1][row-1]+=1
                    # print("delete", delete)
                row-=1
        cnt = 0
        for i in range(n):

            for j in reversed(range(m)):
                if delete[i][j]>=1:
                    graph[i].pop(j)
                    cnt+=1
        # print("graph", graph)
        # print("----")
        answer+=cnt
        if cnt == 0:
            break
        
    
    return answer