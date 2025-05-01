import sys
from collections import defaultdict
input = sys.stdin.readline

p, m = map(int, input().split())

rooms = defaultdict(list)
level, name = input().split()
rooms[name].append((int(level),name))

for i in range(p-1):
    level, name = input().split()
    level = int(level)
    count = 0
    for key in list(rooms.keys()):
        if abs(level - rooms[key][0][0])<=10 and len(rooms[key])<m:
            rooms[key].append((level,name))
            count=0
            break
        count+=1
        if count == len(rooms.keys()):
            rooms[name].append((level,name))
            count=0

for key in list(rooms.keys()):
    if len(rooms[key])>=m:
        print("Started!")
        rooms[key].sort(key = lambda x: x[1])
        for level, name in rooms[key]:
            print(level, name)
    else:
        print("Waiting!")
