# 40m
# Lv2 54%
import heapq
def solution(book_time):
    new_book = []
    for book in book_time:
        new_book.append((int(book[0][:2])*60+ int(book[0][3:]),
                        int(book[1][:2])*60+ int(book[1][3:])))
    
    new_book.sort(key = lambda x: x[0])
    
    hq = []
    cur_rooms = 0
    for book in new_book:
        idx = 0
        if not hq:
            heapq.heappush(hq, book[1])
        else:
            if book[0]<hq[0]+10:
                heapq.heappush(hq, book[1])
            else:
                heapq.heappop(hq)
                heapq.heappush(hq, book[1])
        cur_rooms = max(len(hq), cur_rooms)
        
    return cur_rooms