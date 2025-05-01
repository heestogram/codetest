import sys

n = int(input())

words = []
for i in range(n):
    words.append(sys.stdin.readline().rstrip())

count=0
for i in range(1,n):
    oops=0
    main = [x for x in words[0]]
    for k in words[i]:
        if k in main:
            main.remove(k)
        else:
            oops+=1
    if oops <=1 and len(main)<=1:
        count+=1
print(count)

