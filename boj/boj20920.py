import sys
from collections import defaultdict

n, m = map(int, input().split())

dict = defaultdict(list)

for i in range(n):
    word = sys.stdin.readline().rstrip()
    if len(word)>=m:
        if word not in dict:
            dict[word].append(1)
            dict[word].append(len(word))
        else:
            dict[word][0]+=1

result = list(dict.keys())

result.sort(key = lambda x: (-dict[x][0], -dict[x][1], x))

for item in result:
    print(item)