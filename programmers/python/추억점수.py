from collections import defaultdict
def solution(name, yearning, photo):
    answer = []
    dict = defaultdict(int)
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
        
    for row in photo:
        score = 0
        for col in row:
            score += dict[col]
        answer.append(score)
    return answer