# link : https://school.programmers.co.kr/learn/courses/30/lessons/42586

import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    days = deque([])
    
    for idx,progress in enumerate(progresses):
        days.append(math.ceil((100 - progress ) / speeds[idx]))
    count = 1
    
    if len(days) == 1:
        return [1]

    maxValue = days.popleft()
    
    
    while days:
        currentValue = days[0]
        
        if maxValue >= currentValue:
                count += 1
        else:
            maxValue = currentValue
            answer.append(count)
            count = 1
            
        if len(days) == 1:
            answer.append(count) 
            
        days.popleft()
            
    return answer