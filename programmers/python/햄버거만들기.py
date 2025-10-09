# 1h
def solution(ingredient):
    answer = 0

    i=3
    while i < len(ingredient):

        if ingredient[i]==1:
            if ingredient[i-3:i+1]==[1,2,3,1]:
                answer+=1
                ingredient.pop(i-3)
                ingredient.pop(i-3)
                ingredient.pop(i-3)
                ingredient.pop(i-3)
                i-=2
            else:
                i+=1
        else:
            i+=1

    return answer

# 더 빠른 풀이
def solution(ingredient):
    answer = 0
    stack = []
    for ing in ingredient:
        stack.append(ing)
        if stack[-4:]==[1,2,3,1]:
            answer+=1
            for _ in range(4):
                stack.pop() 
            

    return answer