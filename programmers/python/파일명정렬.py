# 1h
# Lv2 59% 못 풂.
from collections import defaultdict
def solution(files):
    n_list = "1234567890"
    answer = []
    dic = defaultdict(list)
    for f in files:
        n = len(f)
        for idx in range(n):
            if f[idx] in n_list:
                dic[f].append(f[:idx].lower())
                break
        cnt = 0
        k = idx
        while k<n and f[k] in n_list and cnt<5:
            k+=1
            cnt+=1
        dic[f].append(int(f[idx:k]))
    files.sort(key = lambda x: (dic[x][0], dic[x][1]))
    return files