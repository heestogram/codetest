from collections import defaultdict
def solution(players, callings):
    answer = []
    rank = defaultdict(int)
    for i,name in enumerate(players):
        rank[name]=i
    for call in callings:
        calls_rank=rank[call]
        rank[call]-=1
        rank[players[calls_rank-1]]+=1
        players[calls_rank],players[calls_rank-1]=players[calls_rank-1],players[calls_rank]
    return players