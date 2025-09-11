def solution(id_list, report, k):

    n=len(id_list)
    result = [[False]*n for _ in range(n)]
    
    for rep in report:
        reporter, bad = rep.split(" ")
        if not result[id_list.index(reporter)][id_list.index(bad)]:
            result[id_list.index(reporter)][id_list.index(bad)]=True
    prohibit=[]
    for i in range(n):
        count=0
        for j in range(n):
            if result[j][i]:
                count+=1
        if count>=k:
            prohibit.append(i)

    answer=[]
    for res in result:
        count=0
        for p in prohibit:
            if res[p]:
                count+=1
        answer.append(count)
    return answer