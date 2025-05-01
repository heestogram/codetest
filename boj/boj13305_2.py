n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

total = price[0]*length[0]
cur = price[0]

for i in range(1,n-1):
    if price[i]<=cur:
        cur = price[i]
        total += cur*length[i]
    else:
        total += cur*length[i]


print(total)