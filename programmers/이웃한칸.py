def solution(board, h, w):
    answer = 0
    now = board[h][w]
    dh=[1,-1,0,0]
    dw=[0,0,1,-1]
    n=len(board)
    for i in range(4):
        nh=h+dh[i]
        nw=w+dw[i]
        if 0<=nh<=n-1 and 0<=nw<=n-1:
            if now==board[nh][nw]:
                answer+=1
    return answer