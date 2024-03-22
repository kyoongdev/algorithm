from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

R, C = list(map(int,input().split()))


boards = []
for _ in range(R):
  boards.append([x for x in input()])


dx = [-1,1,0,0]
dy = [0,0,-1,1]
maxCount = 0

def dfs(start,move):
  global maxCount 
  x,y = start
  # print(x,y,move)
  maxCount = max(maxCount,len(move))

  for i in range(4):
    nx,ny = x + dx[i], y + dy[i]

    if 0 <= nx < R and 0 <= ny < C and boards[nx][ny] not in move:
      copiedMoved = move.copy()
      copiedMoved.add(boards[nx][ny])
      dfs((nx,ny),copiedMoved)

dfs((0,0),{boards[0][0]})
print(maxCount)