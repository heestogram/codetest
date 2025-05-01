num = input()


n=0
j=0
while True:
    n+=1
    for i in str(n):
        if i == num[j]:
            j+=1


            if j==len(num):
                print(n)
                exit()