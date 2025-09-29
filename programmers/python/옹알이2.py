# 22m
def solution(babbling):
    answer = 0
    able = {"a":"aya","y":"ye","w":"woo","m":"ma"}
    for bab in babbling:
        cur = 0
        past_word = None
        while cur<=len(bab):
            if cur == len(bab):
                answer+=1
                break
            if bab[cur] in list(able.keys()):

                word = able[bab[cur]]
                if cur+len(word)>len(bab) or past_word==word:
                    break
                else:
                    past_word = word
                    if bab[cur:cur+len(word)]==word:
                        cur+=len(word)
                    else:
                        break
            else:
                break
                
    
    return answer