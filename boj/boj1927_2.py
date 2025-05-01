import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

heap = deque()

for i in range(n):
    x = int(input())
    if x>0:
        heap.append(x)
        now = len(heap)-1
        while now>0:
            parent = now//2 
            if heap[parent]>heap[now]:
                heap[now],heap[parent] = heap[parent],heap[now]
                now = parent
            else:
                break

    if x==0:
        if len(heap)>0:
            print(heap.popleft())
        else:
            print("0")