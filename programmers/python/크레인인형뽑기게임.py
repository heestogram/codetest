# 13m
# Lv1 54%
def solution(board, moves):
    answer = 0
    stack = [0]
    
    for mov in moves:
        h = 0
        while h < len(board):
            catch = board[h][mov-1]
            if catch!=0:
                if stack[-1] == catch:
                    stack.pop()
                    answer+=2
                else:
                    stack.append(catch)
                board[h][mov-1]=0
                break
            else:
                h+=1
                
    return answer