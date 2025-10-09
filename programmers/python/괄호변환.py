# 1h 20m 아쉽게 못 풂
# Lv2 48%

def solution(p):
    answer = ''

    def check(word):
        proper=0
        for w in word:
            if w =="(":
                proper+=1
            else:
                proper-=1
            if proper<0:
                return False
        return True
    
    def split_uv(s):
        bal = 0
        for i, ch in enumerate(s):
            bal += 1 if ch == '(' else -1
            if bal == 0:
                return s[:i+1], s[i+1:]
        return s, '' 

    if check(p):
        return p
    
    def dfs(cur):
        if cur == "":
            return ""
        
        u,v = split_uv(cur)

        if check(u):
            return u + dfs(v)
        else:
            reverse = u[1:-1]
            reverse2=""
            for r in reverse:
                if r == "(":
                    reverse2+=")"
                else:
                    reverse2+="("
            return "("+dfs(v)+")"+reverse2
            

    
    return dfs(p)
    
