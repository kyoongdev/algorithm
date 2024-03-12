from collections import deque

widthHeight = input().split(" ")
N = int(widthHeight[0])
M = int(widthHeight[1])

paper = []
maxNumbers= []
for n in range(N):
  p = [int(x) for x in input().split(" ")]
  maxV = max(p)
  maxNumbers.append(maxV)
  paper.append(p)
  
maxNumber = max(maxNumbers)

maxIndexes = []  

for n in range(N):
  for m in range(M):
    if paper[n][m] == maxNumber:
      maxIndexes.append((n,m))

output = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(nodes,start,result,visited,realStart):
  cx,cy = start
  
  if len(result) == 4:
    output.append(result.copy())
    return
  
  for i in range(4):
    nx = cx + dx[i]
    ny = cy + dy[i]

    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
      result.append(nodes[nx][ny])
      visited[nx][ny] = True
      dfs(nodes,(nx,ny), result,visited,realStart)
      visited[nx][ny] = False
      result.pop()
      
def spin(blocks):

  spin90 = []
  spin180 = []
  spin270 = []
  
  for x,y in blocks:
    spin90.append((y,-x))
    spin180.append((-x,-y))
    spin270.append((-y,x))
    
  return spin90,spin180,spin270
    
  
      
def chulShape(start):
  x,y = start
  startPoints = [[(0,1),(0,2),(1,1)],
                 [(1,0),(2,0),(1,1)],
                 [(0,-1),(0,-2),(1,-1)],
                 [(-1,0),(-2,0),(-1,1)],
                 
                 [(0,1),(0,2),(1,-1)],
                 [(1,0),(2,0),(1,-1)],
                 [(0,-1),(0,-2),(-1,-1)],
                 [(-1,0),(-2,0),(-1,-1)],
                 
                 [(-1,0),(0,1),(0,2)],
                 [(0,-1),(1,0),(-1,0)],
                 [(0,-1),(-1,0),(0,1)],
                 [(-1,0),(1,0),(0,1)],]
  
  searchPoints = []
  
  for point in startPoints:
    
    points = [(x,y)]
    for dx,dy in point:
      nx = x + dx
      ny = y + dy
      points.append((nx,ny))
    searchPoints.append(points)
  
  resultPoints = []
  for point in searchPoints:
    spin90,spin180,spin270 = spin(point)
    resultPoints.append(point)
    resultPoints.append(spin90)
    resultPoints.append(spin180)
    resultPoints.append(spin270)

  for sp in resultPoints:
    tmpResult = []
    for x,y in sp:
      if 0 <= x < N and 0 <= y < M:
        tmpResult.append(paper[x][y])
    
    if len(tmpResult) == 4:
      output.append(tmpResult)
      
  

for mIdx in maxIndexes:
  x,y = mIdx
  visited = [[False] * M for _ in range(N)]
  visited[x][y] = True
  dfs(paper,mIdx,[paper[x][y]],visited,mIdx)
  chulShape(mIdx)


maxSum = 0
for o in output:
  # print(o)
  oSum = sum(o)
  if maxSum < oSum:
    maxSum = oSum
    
print(maxSum)
  
   