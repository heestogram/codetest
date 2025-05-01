import sys
from collections import deque

n,k = map(int,input().split())

total = list(sys.stdin.readline())
count=0
# for i in range(n):
#     if total[i] == "H":
#         burger.append(i)
for i in range(n):
    if total[i]=="P":
        for j in range(max(i-k,0),min(i+k+1,n)):
            if j != i and total[j]=="H":
                total[j]="X"
                count+=1
                break

print(count)

