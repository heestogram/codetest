import sys
import heapq
input = sys.stdin.readline

n = int(input())

heap = []

for i in range(n):
    items = list(map(int, input().split()))
    if not heap:
        for j in items:
            heapq.heappush(heap, j)
    else:
        for j in items:
            if j>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, j)

print(heap[0])

