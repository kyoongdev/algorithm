# link : https://school.programmers.co.kr/learn/courses/30/lessons/12909

from collections import deque

def solution(s):
    answer = True
    queue = deque([])
    
    for v in s:
        queue.append(v)
    isClosed = False
    openCount = 1
    closeCount =0
    
    used = list(queue.copy())
    # used = []
    totalOpenCount = 0
    totalCloseCount = 0
    copied =queue.copy()
    while copied:
        value = copied.popleft()
        if value == "(":
            totalOpenCount += 1
        else:
            totalCloseCount += 1
            
    if queue[0] == ")":
        return False
    queue.popleft()
    closed = deque([])
    while queue:
        currentValue = queue.popleft()
        if currentValue == "(":
            closed.append(False)
        else:
            if len(closed) > 0:
                closed.pop()
        
    if len(closed) > 0:
        answer = False

    if answer and totalOpenCount != totalCloseCount:
        return False

    return answer