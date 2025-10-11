# 35m
# Lv1 52%
import re
def solution(new_id):
    answer = ''
    temp1 = new_id.lower()
    temp2 = re.sub(r'[^a-z0-9\.\_\-]', '', temp1)
    stack = [temp2[0]]

    for i in range(1,len(temp2)):
        if temp2[i-1] == temp2[i]==".":
            continue
        else:
            stack.append(temp2[i])

    if stack and stack[0]==".":
        stack.pop(0)
    if stack and stack[-1]==".":
        stack.pop()
    if not stack:
        stack.append('a')
    temp5 = ''.join(stack)
    
    if len(temp5)>=16:
        temp6 = temp5[:15]
        if temp6[-1]==".":
            temp6 = temp6[:-1]
    elif len(temp5)<=2:
        while len(temp5)<3:
            temp5 += temp5[-1]
        temp6 = temp5
    else:
        temp6 = temp5
    

            
    return temp6