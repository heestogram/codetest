def solution(lottos, win_nums):
    zero = lottos.count(0)
    lottos_set = set(lottos)
    win_nums_set = set(win_nums)
    
    matched = len(lottos_set & win_nums_set)
    
    max_match = matched + zero
    min_match = matched

    def rank(x):
        return 7 - x if x >= 2 else 6
    
    return [rank(max_match), rank(min_match)]
