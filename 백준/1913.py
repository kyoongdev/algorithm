N = int(input())
target = int(input())

mid = N // 2

maps = [[0] * N for _ in range(N)]

maps[mid][mid] = 1
start = (mid - 1,mid - 1)

rotate = [(0,1),(1,0),(0,-1),(-1,0)]
direction = 2
count = 2
targetIndex = []
while True:
  x,y =start
  cx,cy = x,y

  if x < 0 and y < 0:
    break
  for rx,ry in rotate:
    for i in range(direction):
      x += rx
      y += ry

      maps[x][y] = count
      if count == target:
        targetIndex = [x + 1,y + 1]
      count += 1
      if x == 0 and y == 0:
        break

  direction += 2
  start = (cx - 1, cy - 1)


if target == 1:
  targetIndex = [mid + 1,mid + 1]

for m in maps:
  print(*m)
print(*targetIndex)