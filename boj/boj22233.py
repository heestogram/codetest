import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# keywords = set([input().rstrip() for _ in range(n)])

# for i in range(m):
#     contents = set(input().rstrip().split(","))
#     keywords -= contents
    
#     print(len(keywords))


keywords = {}
for i in range(n):
    keywords[input().rstrip()]=0

use = 0
for _ in range(m):
    contents = set(input().rstrip().split(","))
    for content in contents:
        if content in keywords.keys():
            if keywords[content]==0:
                keywords[content]=1
                use += 1

    print(n-use)
    