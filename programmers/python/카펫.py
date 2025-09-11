def solution(brown, yellow):
    answer = []
    deno=1
    while yellow/deno>=deno:
        w=yellow/deno
        h=deno
        if (w+h)*2+4==brown:
            break
        deno+=1
            
    answer.append(w+2)
    answer.append(h+2)
    return answer