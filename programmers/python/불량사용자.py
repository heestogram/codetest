
# 1h Lv3  52%
import copy
from collections import defaultdict

def solution(user_id, banned_id):
    # 각 banned 패턴마다 가능한 후보 user 리스트
    answer = []
    for b_id in banned_id:
        candidates = []
        for u in user_id:
            if len(u) != len(b_id):
                continue
            ok = True
            for uc, bc in zip(u, b_id):
                if bc != '*' and uc != bc:
                    ok = False
                    break
            if ok:
                candidates.append(u)
        answer.append(candidates)

    results = set()
    used = set()

    def dfs(idx):
        if idx == len(banned_id):
            results.add(frozenset(used))   # 순서 무시, 집합으로 저장
            return
        for u in answer[idx]:
            if u in used:
                continue
            used.add(u)
            dfs(idx + 1)
            used.remove(u)

    dfs(0)
    return len(results)
