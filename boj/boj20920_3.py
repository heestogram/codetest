import sys
from collections import defaultdict

n, m = map(int, input().split())

word = [sys.stdin.readline().rstrip() for i in range(n)]

word_list = defaultdict(int)

for w in word:
    if len(w)>=m:
        word_list[w]+=1

word_keys = list(word_list.keys())

word_keys.sort(key=lambda x: (-word_list[x], -len(x), x))

for w in word_keys:
    print(w)