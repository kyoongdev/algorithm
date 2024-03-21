import sys
input = sys.stdin.readline

N,M = list(map(int,input().split()))

maps = []
for _ in range(N):
  maps.append(list(map(int,input().split())))



sums = [[0] *( N + 1) for _ in range(N + 1)]
for x in range(1,N+1):
  for y in range(1,N+1):
    sums[x][y] = sums[x][y-1] + sums[x-1][y] - sums[x-1][y-1] +maps[x-1][y-1]



for _ in range(M):
  x1,y1,x2,y2 = tuple(map(int,input().split()))

  if x1 == x2 and y1 == y2:
    print(maps[x2 -1 ][y2 - 1])

  else:
    print(sums[x2][y2] - sums[x2][y1- 1] - sums[x1-1][y2] + sums[x1-1][y1 -1])

  
