import sys

n = int(sys.stdin.readline())

time = []


time = list(map(int,sys.stdin.readline().split()))

time.sort()

wait = 0
for j in range(n):
    wait += sum(time[0:j+1])

print(wait)