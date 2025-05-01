import sys
n = int(input())

for i in range(n):
    ch = input()
    if ch == "KBS1":
        idx1=i
    elif ch == "KBS2":
        idx2=i

result=""

result+=idx1*"1"
result+=idx1*"4"

if idx1>idx2:
    idx2+=1

result+=idx2*"1"
result+=(idx2-1)*"4"

print(result)