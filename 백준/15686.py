from itertools import combinations
from collections import deque
import copy

N,M = tuple(map(int,input().split(" ")))

cities = []
for _ in range(N):
  cities.append(list(map(int,input().split(" "))))

chickens = []
homes = []
for x in range(N):
  for y in range(N):
    if cities[x][y] == 2:
      chickens.append((x,y))
    if cities[x][y] == 1:
      homes.append((x,y))

def getDistance(home,chickens):

  hx,hy = home
  minValue = 1e10

  for c in chickens:
    cx,cy = c
    distance = abs(hx - cx) + abs(hy - cy)
    if distance < minValue:
      minValue = distance

  return minValue

def dfs(cCity,start, visited,count,minCount):
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  x,y = start
  # print(cCity[x][y])
  if cCity[x][y] == 2:
    # print("도착")
    if minCount[0] > count:
      minCount[0] = count
    return

  visited[x][y] = True
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:

      dfs(cCity,(nx,ny), visited, count + 1,minCount)
      visited[nx][ny] = False
  


selectedChickens =list(combinations(chickens,M))
minDistance = 1e10
# print(selectedChickens)
for sc in selectedChickens:
  visited = [[False] * N for _ in range(N)]
  
  cCity = copy.deepcopy(cities)
  for x in range(N):
    for y in range(N):
      if cCity[x][y] == 2 and (x,y) not in list(sc):
        cCity[x][y] = 0
  count = 0
  for h in homes:
    minCount = [1e10]
    dfs(cCity,h,visited,0, minCount)
    count += minCount[0]
  # print(count)

  if count < minDistance:
    minDistance = count
  # distance = 0
  # for h in homes:
  #   distance += getDistance(h,list(sc))

  # if distance < minDistance:
  #   minDistance = distance

print(minDistance)
  
    
  
  


