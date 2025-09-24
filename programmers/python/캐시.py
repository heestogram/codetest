from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cash = deque()
    for city in cities:
        city = city.lower()
        if city in cash:
            cash.remove(city)
            answer+=1
        else:
            answer+=5
        cash.append(city)
        if len(cash)>cacheSize:
            cash.popleft()
    return answer