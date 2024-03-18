
# link : https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque

def solution(prices):
    times = []
    N = len(prices)
    for i in range(N):
        count = 0
        for j in range(i+1,N):
            count += 1
            if prices[j] < prices[i]:
                break
                
        times.append(count)

    return times