import sys
input = sys.stdin.readline

M,N = list(map(int,input().split()))

maps = []
for _ in range(M):
  maps.append(list(map(int,input().split())))



dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
  global dp
  if x == M - 1 and y == N - 1:
    return 1

  if dp[x][y] != -1:
    return dp[x][y]
  way = 0
  for i in range(4):
    nx,ny = x + dx[i], y + dy[i]
    
    if 0 <= nx < M and 0 <= ny < N and maps[x][y] > maps[nx][ny]:
      way += dfs(nx,ny)
  dp[x][y] = way
  
  return dp[x][y]

dp = [[-1] * N for _ in range(M)]
print(dp)
print(dfs(0,0))
  


