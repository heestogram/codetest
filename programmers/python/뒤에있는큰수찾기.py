# 1h +
def solution(numbers):

    rear = []
    n = len(numbers)
    answer = [-1]*n
    for i in range(n-1,-1,-1):
        cur = numbers[i]
        while rear and rear[-1]<=cur:
            rear.pop()
        answer[i]=rear[-1] if rear else -1
        rear.append(cur)
    return answer