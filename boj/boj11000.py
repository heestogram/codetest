import sys, heapq

n = int(input())

classes = []

for i in range(n):
    s, t = map(int, sys.stdin.readline().split())
    classes.append((s,t))

classes.sort(key=lambda x: (x[0],x[1]))

heap = [classes[0][1]]

for j in range(1, n):
    if heap[0] <= classes[j][0]:
        heapq.heappop(heap)
    heapq.heappush(heap, classes[j][1])

print(len(heap))
