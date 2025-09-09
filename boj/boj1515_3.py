num = input()


cur = 0
idx = 0
length = len(num)
while True:
    cur+=1
    for c in str(cur):
        if c==num[idx]:
            idx+=1
            if idx == length:
                print(cur)
                exit()