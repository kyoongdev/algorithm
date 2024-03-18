import sys
input  = sys.stdin.readline

R,C = list(map(int,input().split()))

board = []

for _ in range(R):
  board.append(input())

dx = [0,1,0,-1]
dy = [1,0,-1,0]
visited = set(board[0][0])
totalCounts = 0

def dfs(nodes,start,count):
  global visited, dx, dy,totalCounts
  x,y = start
  totalCounts = max(totalCounts,count)
  
  if count == R * C:
    return

  for i in range(4):
    nx,ny = x + dx[i],y + dy[i]

    if 0 <= nx < R and 0 <= ny < C and nodes[nx][ny] not in visited:
      visited.add(nodes[nx][ny])
      dfs(nodes,(nx,ny),count + 1)
      visited.remove(nodes[nx][ny])

dfs(board,(0,0), 1)
print(totalCounts)

