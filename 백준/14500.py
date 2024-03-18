from collections import deque
import sys
input = sys.stdin.readline

N, M = list(map(int,input().split()))

paper =  []
for _ in range(N):
  paper.append(list(map(int,input().split())))

def rotate(block):
  spin90,spin180,spin270 = set(),set(),set()

  while block:
    x,y = block.pop()
    spin90.add((y,-x))
    spin180.add((-x,-y))
    spin270.add((-y,x))
  return spin90,spin180,spin270

def normalize(block):
  minX, minY = min(block)
  newBlock = [(x - minX, y - minY) for x,y in block]
  newBlock.sort()
  return newBlock


## 볼록할 철자 모양
tetroExcluded = [[(0,0),(0,1),(0,2),(1,1)], [(0,0),(0,1),(0,2),(-1,1)],[(0,0),(0,1),(0,2),(0,3)], [(0,0),(0,1),(1,0),(1,1)], [(0,0),(1,0),(2,0),(2,1)],[(0,0),(1,0),(2,0),(2,-1)],[(0,0),(1,0),(1,1),(2,1)],[(0,0),(1,0),(1,-1),(2,-1)] ]
tetroExcludeds = []
for te in tetroExcluded:
  spin90, spin180,spin270 = rotate(set(te))
  tetroExcludeds.append(te)
  tetroExcludeds.append(normalize(spin90))
  tetroExcludeds.append(normalize(spin180))
  tetroExcludeds.append(normalize(spin270))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(nodes,start,visited,counts,output,count):
  global N,M
  sx,sy = start

  if sum(counts) > count:
    return

  if len(counts) == 4:
    output.add(sum(counts))
    return

  for i in range(4):
    nx,ny = sx + dx[i], sy + dy[i]
    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
      visited[nx][ny] = True
      dfs(nodes,(nx,ny),visited,[*counts, nodes[nx][ny]],output, count + nodes[nx][ny] )
      visited[nx][ny] = False


def checkChul(nodes,start):
  global tetroExcludeds,N,M
  x,y = start
  counts = []
  for te in tetroExcludeds:

    one,two,three,four = te
    ox,oy = one
    tx,ty = two
    thx,thy = three
    fx,fy = four
    ox,oy = ox + x, oy + y
    tx,ty = tx + x, ty + y
    thx,thy = thx + x, thy + y
    fx,fy = fx + x, fy + y

    if 0<= ox < N and 0 <= oy < M and 0<= tx < N and 0 <= ty < M and 0<= thx < N and 0 <= thy < M and 0<= fx < N and 0 <= fy < M :
      counts.append(nodes[ox][oy] + nodes[tx][ty] + nodes[thx][thy] + nodes[fx][fy])
  if len(counts) == 0:
    return 0
  else:
    return max(counts)



## 각 노드마다 테트로미노 조회
maxCount = 0
for x in range(N):
  for y in range(M):
    
    chulCount = checkChul(paper,(x,y))
    maxCount = max(maxCount,chulCount)

print(maxCount)


"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
max_num = max(map(max, board))

d = [(-1, 0), (1, 0), (0, -1), (0, 1)]
answer = 0

def dfs(r, c, cnt, res):
    global answer
    if res + (4 - cnt) * max_num < answer:
        return
    
    if cnt == 4:
        answer = max(answer, res)
        return
    
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] > 0:
            temp = board[nr][nc]
            if cnt == 2:
                board[nr][nc] = 0
                dfs(r, c, cnt + 1, res + temp)
                board[nr][nc] = temp
            
            board[nr][nc] = 0
            dfs(nr, nc, cnt + 1, res + temp)
            board[nr][nc] = temp
    
def solution():
    for i in range(N):
        for j in range(M):
            temp = board[i][j]
            board[i][j] = 0
            dfs(i, j, 1, temp)
            board[i][j] = temp
    return answer

print(solution())

"""