from collections import defaultdict, deque

def solution(friends, gifts):
        
    dic = defaultdict(list)
    answer = defaultdict(int)
    
    for gift in gifts:
        give, given = gift.split(" ")
        dic[give].append(given)
    while friends:
        friend = friends.pop()
        for f in friends:
            if dic[friend].count(f)>dic[f].count(friend):
                answer[friend]+=1
            elif dic[friend].count(f)<dic[f].count(friend):
                answer[f]+=1
            else:
                friend_idx = len(dic[friend])-sum(list(dic.values()),[]).count(friend)

                f_idx = len(dic[f])-sum(list(dic.values()),[]).count(f)
                if friend_idx>f_idx:
                    answer[friend]+=1
                elif f_idx>friend_idx:
                    answer[f]+=1
                    
    result = list(answer.values())
    if result:
        return max(result)
    else:
        return 0
