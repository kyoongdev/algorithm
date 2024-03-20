from collections import deque

N, M = list(map(int,input().split()))


maps = []
for _ in range(N):
  maps.append([int(x) for x in input()])


visited = [[[False] * 2 for _ in range(M)]  for _ in range(N)] 


queue = deque([(0,0,1,1)])
dx = [-1,1,0,0]
dy = [0,0,-1,1]
moveCount = 0
isDone = False

while queue:
  x,y,breakCount,move = queue.popleft()

  if x == N - 1 and  y == M - 1:
    moveCount = move
    isDone = True
    break

  for i in range(4):
    nx,ny = x + dx[i], y + dy[i]

    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny][breakCount]:
      if maps[nx][ny] == 0:
        visited[nx][ny][breakCount] = True
        queue.append((nx,ny,breakCount,move + 1))
      else:
        if breakCount == 1:
          visited[nx][ny][breakCount - 1] = True
          queue.append((nx,ny,breakCount - 1,move + 1))
      
  
  
if isDone:
  print(moveCount)
else : 
  print(-1)