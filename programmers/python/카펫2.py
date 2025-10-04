def solution(brown, yellow):
    answer = []
    
    summ = brown+yellow
    w = summ
    h = 3
    while h<=w:
        if summ%h==0:
            w = summ/h
            if 2*w + 2*(h-2) == brown:
                return [w,h]
        h+=1