from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

maps = []
for _ in range(N):
  maps.append([x for x in input()][:-1])

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(start,visited,flag):
  global maps,dx,dy
  cx,cy = start
  visited[cx][cy] = True

  queue = deque([start])
  count = 1
  while queue:
    x,y= queue.popleft()

    for i in range(4):
      nx,ny = x + dx[i], y + dy[i]
      if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and maps[nx][ny] == flag:
        visited[nx][ny] = True
        count += 1
        queue.append((nx,ny))

  return count

visited = [[False] * N for _ in range(N)]
answer = []
for x in range(N):
  for y in range(N):
    if maps[x][y] != '0' and not visited[x][y]:
      count = bfs((x,y),visited,maps[x][y])
      answer.append(count)

    
print(len(answer))
answer.sort()
for a in answer:
  print(a)
    
