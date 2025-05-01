n = int(input())

num = (n-1)/6

if n==1:
    print(1)
    exit()


a=0
count=0

for i in range(1,n):
    a+=i
    result=num-a
    count+=1
    if result<=0:
        break


#1 8.x
#2 5.x
#3 
print(count+1)