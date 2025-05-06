def solution(targets):
    answer = 0
    targets.sort(key=lambda x: (x[1],x[0]))
    n = len(targets)
    cur_end=targets[0][1]
    for i in range(1,n):
        if targets[i][0]>=cur_end:
            answer+=1
            cur_end = targets[i][1]

    return answer+1