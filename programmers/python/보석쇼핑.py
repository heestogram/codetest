# 1h+ 못풂
# Lv3 52%
from collections import defaultdict

def solution(gems):
    uniq = len(set(gems))       
    n = len(gems)

    temp = float('inf')
    start, best_start = 0, 0
    end, best_end = 0, n

    freq = defaultdict(int)
    have = 0

    while end < n:
        g = gems[end]
        freq[g] += 1
        if freq[g] == 1:            # 새 종류가 처음 들어옴
            have += 1
        end += 1

        # 모든 종류를 포함했다면 왼쪽을 최대한 줄이기
        while have == uniq and start < end:
            if end - start < temp:
                temp = end - start
                best_start, best_end = start, end 

            left = gems[start]
            freq[left] -= 1
            start += 1
            if freq[left] == 0:    
                have -= 1

    return [best_start + 1, best_end]
