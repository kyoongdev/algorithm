# link : https://school.programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque([])
    cities = deque([c.lower() for c in cities])
    if cacheSize == 0:
        return len(cities) * 5

    while cities:
        city = cities.popleft()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        ## 캐시가 아직 꽉 차지 않은 경우
        elif len(cache) < cacheSize:
            answer += 5
            cache.append(city)
        ## 캐시가 꽉 찬 경우
        else:
            answer += 5
            cache.popleft()
            cache.append(city)

    # print(answer,cache)

    return answer
