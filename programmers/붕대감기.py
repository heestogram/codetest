def solution(bandage, health, attacks):
    answer = health
    t = 0
    contin = 0
    j=0
    while j<len(attacks):
        t+=1
        if t == attacks[j][0]:
            answer -= attacks[j][1]
            j+=1
            contin = 0
            if answer <= 0:
                answer=-1
                break
            continue

        answer = min(answer+bandage[1],health)
        contin+=1
        if contin == bandage[0]:
            answer = min(answer+bandage[2],health)
            contin=0
            
    return answer