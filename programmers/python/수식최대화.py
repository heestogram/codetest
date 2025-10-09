# 1h 20m 못 풂
# Lv 2 49%
from collections import deque
from itertools import permutations
import copy
def solution(expression):
    
    def calc(left, right, target):
        if target=="+":
            return left+right
        elif target=="-":
            return left-right
        return left*right
        
    word = ""
    wlist = []
    olist = []
    for i in range(len(expression)):
        exp = expression[i]
        if exp in ["+","-","*"]:
            wlist.append(int(word))
            olist.append(exp)
            word=""
        else:
            word+=exp
        if i == len(expression)-1:
            wlist.append(int(word))
    
    uniq_op = set(olist)
    ans=0
    
    for order in permutations(uniq_op):
        op = copy.deepcopy(olist)
        wo = copy.deepcopy(wlist)
        for o in order:
            j=0
            while j<len(op):
                if o == op[j]:
                    res = calc(wo[j], wo[j+1], o)
                    wo[j]=res
                    op.pop(j)
                    wo.pop(j+1)
                else:
                    j+=1
                    
        ans = max(ans, abs(wo[0]))

    return ans
                        
                    
    