# from collections import defaultdict
# def solution(want, number, discount):
#     want = dict(zip(want,number))
#     result=0
    
#     for i in range(len(discount)-9):
#         disc = defaultdict(int)
#         for item in discount[i:i+10]:
#             disc[item]+=1
#         cnt=0    
#         for k in want.keys():
#             if want[k]<=disc[k]:
#                 cnt+=1
#         if cnt==len(want):
#             result+=1
                
        
#     return result

# 16m 00s

from collections import defaultdict
def solution(want, number, discount):
    want = dict(zip(want,number))
    result=0
    
    for i in range(len(discount)-9):
        disc = defaultdict(int)
        for item in discount[i:i+10]:
            disc[item]+=1

        if want==disc:
            result+=1
                
        
    return result