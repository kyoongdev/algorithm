# link :  https://www.acmicpc.net/problem/7576
import sys 
from collections import deque

input = sys.stdin.readline

M,N = list(map(int,input().split()))

tomato = []
for _ in range(N):
  tomato.append(list(map(int,input().split())))

# 1 : 익은 토마토, 0 : 익지 않은 토마토, -1 : 토마토 없음

# 익은 토마토의 위치 찾기
# 하루 지나면서 익은 토마토 하나씩 퍼트리기
# 다 익었는지 여부 체크

goodTomato = []
for x in range(N):
  for y in range(M):
    if tomato[x][y] == 1:
      goodTomato.append((x,y))

if len(goodTomato) == 0:
  print(-1)
  exit()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

travel = [0]
def bfs(starts):
  global tomato,timeDict,travel

  time = 0  
  targets = deque([starts])

  while targets:
    ts = targets.popleft()

    tmp = []
    for x,y in ts:
      for i in range(4):
        nx,ny = x + dx[i] , y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
          tomato[nx][ny] = 1
          tmp.append((nx,ny))

    if len(tmp) > 0:
      time += 1
      targets.append(tmp)

  return time

time = bfs(goodTomato)

isZeroExists = False
for x in range(N):
  for y in range(M):
    if tomato[x][y] == 0:
      isZeroExists = True

if isZeroExists:
  print(-1)
else:
  print(time)

