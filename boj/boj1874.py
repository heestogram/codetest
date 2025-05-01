import sys
n = int(sys.stdin.readline())

stack = []
result = []
point = 0
avail = True
for i in range(n):
    num = int(sys.stdin.readline())
    while point < num:
        point += 1
        stack.append(point)
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        avail = False

if avail:
    for j in result:
        print(j)
else: print("NO")
