# 15m
# Lv2 70%
def solution(n,a,b):
    answer = 0
    cnt=0
    k=n
    while k!=1:
        k=k/2
        cnt+=1
    
    square=1
    game=cnt
    while True:
        if square==cnt:
            break
        mid = n/(2**square)+0.1
        check = [a,b,mid]
        check.sort()
        if check[1]==mid:
            return game
        elif check[0]==mid:
            a-=(mid-0.1)
            b-=(mid-0.1)
        game-=1
        square+=1
    
    return game