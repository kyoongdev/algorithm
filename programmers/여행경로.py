from collections import deque
from collections import defaultdict
def solution(tickets):
    answer = []
    ticketDict = defaultdict(list)
    
    
    for idx,ticket in enumerate(tickets):
        start = ticket[0]
        end = ticket[1]
        ticketDict[start].append([end,idx])
        
    for key in ticketDict.keys():
        ticketDict[key].sort()
        
    output = []
    def dfs(start,visited,path):
        nonlocal output
        if output:
            return
        if len(path) == len(tickets) + 1:
            output = path.copy()
            return
        for idx,place in enumerate(ticketDict[start]):
            if not visited[place[1]]:
                visited[place[1]] = True
                path.append(place[0])
                
                dfs(place[0],visited,path)
                path.pop()
                visited[place[1]] = False

    visited = [False] * len(tickets)
    
    dfs("ICN",visited,["ICN"])    
    
    print("output",output)
        
    return output

