n = int(input())

history = [-1]*10001

history[1]=1
history[2]=0
history[3]=1

for i in range(4,n+1):
    if history[i-1]==1 or history[i-3]==1:
        history[i]=0
    else:
        history[i]=1

if history[n]==1:
    print("SK")
else:
    print("CY")