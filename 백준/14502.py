from itertools import combinations
import copy

N,M = list(map(int,input().split(" ")))

maps = []
for _ in range(N):
  maps.append(list(map(int,input().split(" "))))

candidates = []
viruses =[]
for x in range(N):
  for y in range(M):
    if maps[x][y] == 0:
      candidates.append((x,y))
    if maps[x][y] == 2:
      viruses.append((x,y))


def spread(cMap,virus):
  global candidates
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  x,y = virus
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < N and 0 <= ny < M and cMap[nx][ny] == 0:
      cMap[nx][ny] = 2
      spread(cMap,(nx,ny))

combis = list(combinations(candidates, 3))
maxZeroCount = 0
for c in combis:
  tMap = copy.deepcopy(maps)

  for t in c:
    x,y = t
    tMap[x][y] = 1
  
  for virus in viruses:
    spread(tMap,virus)
  zeroCount = 0
  for x in range(N):
    for y in range(M):
      if tMap[x][y] == 0:
        zeroCount += 1
  if zeroCount > maxZeroCount:
    maxZeroCount = zeroCount

print(maxZeroCount)

  
  


