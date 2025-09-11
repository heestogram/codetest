def solution(s):
    answer = 0
    for i in range(len(s)):
        if answer<0:
            return False
        if s[i] == "(":
            answer+=1
        else:
            answer-=1
    if answer==0:
        return True
    else:
        return False