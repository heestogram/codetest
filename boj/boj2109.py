import sys

n = int(input())

lecture = []

for i in range(n):
    p, d = map(int, sys.stdin.readline().split())
    lecture.append((p,d))

lecture.sort(key=lambda x: (-x[0],x[1]))

avail = [0]*10001

for i in range(n):
    p, d = lecture[i][0], lecture[i][1]
    for j in range(d,0,-1):
        if avail[j] == 0:
            avail[j] = p
            break

print(sum(avail))