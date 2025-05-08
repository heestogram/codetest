import heapq
def solution(scoville, K):
    heap=[]
    for s in scoville:
        heapq.heappush(heap,s)
    trial=0
    while heap[0]<K:
        if len(heap)==1:
            return -1
        min1 = heapq.heappop(heap)
        min2 = heapq.heappop(heap)
        new = min1 + (min2*2)
        heapq.heappush(heap,new)
        trial+=1
    return trial