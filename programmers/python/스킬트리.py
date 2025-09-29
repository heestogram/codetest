# 38m

def solution(skill, skill_trees):
    answer = 0
    
    def cnt(tree):
        past,cur=-1,-1
        for t in tree:
            if t in skill:
                cur = skill.index(t)
                if cur == past+1:
                    past = cur
                else:
                    return 0 
        return 1
    
    for tree in skill_trees:
        answer+=cnt(tree)


    return answer