import sys, heapq

n = int(sys.stdin.readline())

heap = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap:
            print("0")
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (abs(x),x))