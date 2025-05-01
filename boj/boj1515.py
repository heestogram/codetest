import sys

num = sys.stdin.readline().rstrip()

n=0
idx=0

while True:
    n += 1
    for digit in str(n):
        if num[idx]==digit:
            idx += 1
            if idx == len(num):
                print(n)
                exit()


