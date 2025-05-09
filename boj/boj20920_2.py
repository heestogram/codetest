import sys
from collections import defaultdict
input = sys.stdin.readline

words = defaultdict(int)

n, m = map(int, input().split())
word = [input().rstrip() for i in range(n)]

for w in word:
    if len(w)>=m:
        words[w]+=1


result = list(words.keys())

result.sort(key=lambda x: (-words[x],-len(x),x))

for item in result:
    print(item)