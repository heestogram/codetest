import sys
input = sys.stdin.readline

words = list(input().rstrip())

m = int(input())

# cursor = len(words)

# def active(command, cursor, words):
#     if command[0]=="P":
#         words = words[:cursor]+[command[1]]+words[cursor:]
#         cursor+=1
#     elif command[0]=="L" and cursor!=0:
#         cursor-=1
#     elif command[0]=="D" and cursor!=len(words):
#         cursor+=1
#     elif command[0]=="B" and cursor!=0:
#         words = words[:cursor-1]+words[cursor:]
#         cursor-=1
#     return words, cursor


# for i in range(m):
#     command = list(input().split())
#     words, cursor = active(command, cursor, words)

words2=[]

for _ in range(m):
    command = list(input().split())
    if command[0]=="L":
        if words:
            words2.append(words.pop())
    elif command[0]=="D":
        if words2:
            words.append(words2.pop())
    elif command[0]=="B":
        if words:
            words.pop()
    else:
        words.append(command[1])



words.extend(reversed(words2))

print(''.join(words))


