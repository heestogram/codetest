h,w,n,m = map(int, input().split())


a=0
for i in range(0,w,m+1):
    if i<=w-1:
        a+=1
b=0
for j in range(0,h,n+1):
    if j<=h-1:
        b+=1

print(a*b)