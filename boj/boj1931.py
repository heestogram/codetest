import sys

n = int(sys.stdin.readline())

schedule = []
for i in range(n):
    s, f = map(int, sys.stdin.readline().split())
    schedule.append((s,f))

schedule.sort(key=lambda x: (x[1],x[0]))

finish = 0
count = 0
for time in schedule:
    if time[0] >= finish:
        finish = time[1]
        count += 1

print(count)