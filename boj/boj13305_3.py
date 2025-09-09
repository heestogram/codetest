n = int(input())

length = list(map(int, input().split()))

price = list(map(int, input().split()))

answer=price[0]*length[0]
minim = price[0]
for i in range(1,len(length)):
    if price[i]<minim:
        minim = price[i]
    answer += minim*length[i]

print(answer)
