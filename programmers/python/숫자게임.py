# 35m
# Lv3 59% 못풂
def solution(A, B):
    A.sort()
    B.sort()
    i=j=0
    score = 0
    n = len(A)
    while i<n and j<n:
        if B[j]>A[i]:
            score+=1
            j+=1
            i+=1
        else:
            j+=1
    return score