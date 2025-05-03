def solution(diffs, times, limit):
    answer = 0 
    left = 1
    right = max(diffs)
    
    while left<right:
        level = (left+right)//2
        total=(times[0]*max(1,diffs[0]-level))
        for i in range(1,len(diffs)):
            if diffs[i]<=level:
                total += times[i]
            else:
                total += ((sum(times[i-1:i+1]))*(diffs[i]-level)+times[i])
        print(total, left, level, right)
        if total<=limit:
            right=level
        else:
            left=level+1
    return left