def solution(strings, n):
    answer = strings
    answer.sort(key=lambda x: (x[n],x))
    return answer