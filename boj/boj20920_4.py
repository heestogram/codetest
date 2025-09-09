from collections import defaultdict
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = [input().strip() for i in range(n)]

word_dict = defaultdict(int)

for w in words:
    if len(w)>=m:
        word_dict[w]+=1

result = list(word_dict.keys())

result.sort(key=lambda x: (-word_dict[x], -len(x), x))

for re in result:
    print(re)
