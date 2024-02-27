from collections import deque

## 상하좌우 가능 (중간)
## (오른 아래 )-> 도착
def bfs(maps, startMap,visited,end):
    
    visited[startMap[0]][startMap[1]] = True
    
    if startMap[0] == end[0] and startMap[1] == end[1]:
        return 
    
    up = [startMap[0] - 1,startMap[1]]
    down = [startMap[0] + 1,startMap[1]]
    right = [startMap[0],startMap[1] + 1]
    left = [startMap[0],startMap[1] - 1]
    
    print(startMap)
    ## 하우 가능 (왼쪽 위)
    if startMap[0] == 0 and startMap[1] == 0:
        print("왼쪽 위")
        if maps[down[0]][down[1]] == 0 and maps[right[0]][right[1]] == 0:
            return
        ## 아래로 가는 경우
        elif not visited[down[0]][down[1]] and maps[down[0]][down[1]] == 1:
            bfs(maps,down,visited, end)
        ## 오른쪽으로 가능 경우
        elif not visited[right[0]][right[1]] and maps[right[0]][right[1]] == 1:
            bfs(maps, right,visited, end)
    ## 상우하 가능 (왼쪽 변)
    elif startMap[0] > 0  and startMap[1] < end[0] and startMap[1] == 0:
        print("왼쪽변")
        if (visited[up[0]][up[1]] == True or maps[up[0]][up[1]] == 0) and (visited[down[0]][down[1]] == True or maps[down[0]][down[1]] == 0) and (visited[left[0]][left[1]] == True or maps[right[0]][right[1]] == 0):
            return
        ## 오른쪽으로 가능 경우
        if not visited[right[0]][right[1]] and maps[right[0]][right[1]] == 1:
            bfs(maps, right,visited, end)
        ## 아래로 가능 경우
        if not visited[down[0]][down[1]] and maps[down[0]][down[1]] == 1:
            bfs(maps,down,visited,end)
    ## 상우 가능 (왼쪽 아래)
    elif startMap[0] > 0  and startMap[1] < end[0] and startMap[1] == end[1]:
        ## 우로 가능 경우
        if not visited[right[0]][right[1]] and maps[right[0]][right[1]] == 1:
            bfs(maps, right,visited, end)
    ## 하좌 가능 (오른 위)
    elif startMap[0] == 0 and startMap[1] == end[1]:
        if  (visited[down[0]][down[1]] == True or maps[down[0]][down[1]] == 0) and (visited[left[0]][left[1]] == True or maps[left[0]][left[1]] == 0):
            return
        elif not visited[down[0]][down[1]] and maps[down[0]][down[1]] == 1:
            bfs(maps,down,visited,end)
    ## 상좌하 가능 (오른 변)
    elif startMap[0] > 0  and startMap[1] < end[0] and startMap[1] == end[1]:
        if (visited[up[0]][up[1]] == True or maps[up[0]][up[1]] == 0) and (visited[down[0]][down[1]] == True or maps[down[0]][down[1]] == 0) and (visited[left[0]][left[1]] == True or maps[left[0]][left[1]] == 0):
            return
        ## 위로 가는 경우
        if not visited[up[0]][up[1]] and maps[up[0]][up[1]] == 1 and maps[down[0]][down[1]] == 0:
            bfs(maps,up,visited,end)
        ## 좌로 가는 경우
        elif not visited[left[0]][left[1]] and maps[left[0]][left[1]] == 1 and maps[down[0]][down[1]] == 0:
            bfs(maps,left,visited,end)
        ## 아래로 가는 경우
        elif not visited[down[0]][down[1]] and maps[down[0]][down[1]] == 1:
            bfs(maps,down,visited,end)
    ## 상하좌우 가능(중간)
    elif startMap[0] > 0 and startMap[0] < end[0] and startMap[1] > 0 and startMap[1] < end[1]:
        if (visited[up[0]][up[1]] == True or maps[up[0]][up[1]] == 0) and (visited[down[0]][down[1]] == True or maps[down[0]][down[1]] == 0) and (visited[left[0]][left[1]] == True or maps[left[0]][left[1]] == 0) and (visited[right[0]][right[1]] == True or maps[right[0]][right[1]] == 0):
            return
        
        ## 위로 가는 경우
        if not visited[up[0]][up[1]] and maps[up[0]][up[1]] == 1 and maps[down[0]][down[1]] == 0:
            bfs(maps,up,visited,end)
        ## 좌로 가는 경우
        elif not visited[left[0]][left[1]] and maps[left[0]][left[1]] == 1 and maps[right[0]][right[1]] == 0:
            bfs(maps,left,visited,end)
        ## 아래로 가는 경우
        elif not visited[down[0]][down[1]] and maps[down[0]][down[1]] == 1:
            bfs(maps,down,visited,end)
        ## 아래로 가는 경우
        elif not visited[right[0]][right[1]] and maps[right[0]][right[1]] == 1:
            bfs(maps,down,visited,end)
    else:
        visited[end[0]][end[1]] = True
        return 

def solution(maps):
    answer = 0
    ## 가로 idx
    n = len(maps) - 1
    ## 세로 idx
    m = len(maps[0]) - 1
    visited = [[False] * (n + 1) for x in range(0,m+1)]

    for map in maps:
        print(map)
        
    bfs(maps,[0,0],visited,[n-1,m-1])
    for visit in visited:
        print(visit)
    return answer
  
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])