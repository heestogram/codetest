# 40m
# level 1 70%

def solution(n, arr1, arr2):
    compare=[]
    for arr in [arr1,arr2]:
        result=[]
        for num in arr:
            if num==0:
                result.append(" "*5)
                continue
            square_list=[]
            while num>0:
                square=0
                while True:
                    cur = 2**square
                    if num<cur:
                        break
                    square+=1
                num-=2**(square-1)

                square_list.append(square)
                code = [" "]*n
                for sq in square_list:
                    code[-sq]="#"
            result.append(code)
        compare.append(result)
        
    last = []
    for i in range(n):
        last2=[]
        for j in range(n):
            if compare[0][i][j]=="#" or compare[1][i][j]=="#":
                last2.append("#")
            else:
                last2.append(" ")
        last.append(last2)
    answer=[]
    for l in last:
        a = ""
        for co in l:
            a+=co
        answer.append(a)
    return answer