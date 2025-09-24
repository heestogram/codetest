def solution(a, b):
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(a-1):
        b+=month[i]
    weekday = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    return weekday[b%7-1]