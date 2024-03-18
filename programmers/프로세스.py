# link : https://school.programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    answer = 0
    
    queue = deque([[idx,value] for idx,value in enumerate(priorities)])
    count = 0
    
    while queue:
        target = queue.popleft()
        
        isExistsList = [value for value in queue if value[1] > target[1]]
        if len(isExistsList) > 0:
            queue.append(target)
        else:
            count += 1
            if target[0] == location:
                answer = count
    
        
        
    return answer