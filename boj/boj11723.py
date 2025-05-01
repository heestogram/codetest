import sys

m = int(input())

s = set()
    
for i in range(m):
    input = sys.stdin.readline().strip().split()
    if len(input)==1:
        if input[0]=="all":
            s = set([i for i in range(1,21)])
        else:
            s = set()

    else:
        name = input[0]
        num = int(input[1])

        if name == "add":
            s.add(num)
        if name == "remove":
            s.discard(num)
        if name == "check":
            if num in s:
                print(1)
            else:
                print(0)
        if name == "toggle":
            if num in s:
                s.remove(num)
            else:
                s.add(num)