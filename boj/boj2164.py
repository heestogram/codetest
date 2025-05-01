from collections import deque

n = int(input())
queue = deque()

for i in range(1,n+1):
    queue.append(i)

while len(queue)>1:
    queue.popleft()
    top = queue.popleft()
    queue.append(top)

print(queue[0])


# 큐 안 쓰고 output 규칙성을 보고 짜는 코드
# square = 2

# while True:
#     if (input == 1 or input == 2):
#         print(input)
#         break
#     square *= 2
#     if (square >= input):
#         print((input - (square // 2)) * 2)
#         break
# 출처: https://tooo1.tistory.com/88 [개발자 퉁이리:티스토리]