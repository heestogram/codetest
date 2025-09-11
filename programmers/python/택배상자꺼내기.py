def solution(n, w, num):
    count=1
    cur=num
    while cur<=n:
        if cur%w==0:
            na=w
        else:
            na=cur%w
        cur+=(w-na)*2+1
        if cur<=n:
            count+=1
        
    return count