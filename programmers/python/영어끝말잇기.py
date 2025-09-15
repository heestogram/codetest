from collections import defaultdict
def solution(n, words):
    answer = []
    count = defaultdict(int)
    
    t=0
    for w in words:
        count[w]+=1
        if t>=1:
            if count[w]>1 or words[t][0]!=words[t-1][-1]:
                break
        t+=1
    if t==len(words):
        answer=[0,0]
    else:
        answer.append(t%n+1)
        answer.append(t//n+1)
    return answer