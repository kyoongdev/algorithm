# link : https://school.programmers.co.kr/learn/courses/30/lessons/42583
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    queue = deque(truck_weights)
    bridge = deque([0 for i in range(bridge_length)] , maxlen= bridge_length)
    totalWeight = 0
    while True:
        if len(queue) == 0 :
            time += bridge_length
            break
        
        current = queue[0]
        
        if   totalWeight + current - bridge[0]  <= weight:
            totalWeight += current
            totalWeight -= bridge[0]
            bridge.append(queue.popleft())
        else:
            totalWeight -= bridge[0]     
            bridge.append(0)

        
        time += 1
                
    return time