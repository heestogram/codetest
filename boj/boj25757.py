import sys

n, game = input().split()

n = int(n)

names = []

for i in range(n):
    name = sys.stdin.readline().rstrip()
    names.append(name)

names = list(set(names))

if game == "Y":
    answer = len(names)
if game == "F":
    answer = len(names)//2
if game == "O":
    answer = len(names)//3

print(answer)