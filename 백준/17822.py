from collections import deque
import sys
input = sys.stdin.readline


N,M,T = list(map(int,input().split()))


boards = []

for _ in range(N):
  boards.append(deque(map(int,input().split())))


orders = []

for _ in range(T):
  orders.append(list(map(int,input().split())))

## x,d,k
## x의 배수인 원판, d방향 (0은 시계, 1은 반시계), k칸 회전

## rotate 음수 : 반시계, 양수: 시계

## 5 2 4 2 -> 2 5 2 4

#같은 원
same = [(0,-1),(0,1)]
## 다른 원
diff = [(1,0),(-1,0)]
# print(orders)
answer= 0
for x,d,k in orders:
  targetBoard = x

  while targetBoard <= N:
    # 시계
    if d == 0:
      boards[targetBoard - 1].rotate(k)
    # 반시계
    else:
      boards[targetBoard - 1].rotate(-k)
    targetBoard += x
  erase = set()
  # for b in boards:
    # print(*b)
  for x in range(N):
    for y in range(M):
      
      for i in range(2):
        sx,sy = same[i]
        dx,dy = diff[i]
          
        nsx,nsy = x + sx,y + sy
        dsx,dsy = x + dx,y + dy
        
        if 0 <= nsx < N and 0 <= nsy < M and boards[x][y] != 0 and boards[x][y] == boards[nsx][nsy] :
          erase.add((nsx,nsy))
          erase.add((x,y))
        if nsy > M:
          nsy = 0
          if boards[x][y] != 0 and boards[x][y] == boards[nsx][nsy] :
            erase.add((nsx,nsy))
            erase.add((x,y))
        if nsy < 0:
          nsy = M - 1
          if boards[x][y] != 0 and boards[x][y] == boards[nsx][nsy] :
            erase.add((nsx,nsy))
            erase.add((x,y))


        if 0 <= dsx < N and 0 <= dsy < M and boards[x][y] != 0 and boards[x][y] == boards[dsx][dsy] :
          erase.add((dsx,dsy))
          erase.add((x,y))
  
  # print("erase : ", erase)
  
  # print("result")
  if len(erase) > 0:
    for ex,ey in erase:
      boards[ex][ey] = 0
  else:
    sums = 0
    length = 0 
    for b in boards:
      sums += sum(b)
      length += len([x for x in b if x != 0])
    if length != 0:
    
      avg = sums / length
    # print("avg : ",avg)

      for i in range(N):
        
        for j in range(M):
          if boards[i][j] != 0:
            if boards[i][j] > avg:
              boards[i][j] -= 1
            elif boards[i][j] < avg:
              boards[i][j] += 1
    
  # for b in boards:
    # print(*b)
  # print("")

answer = 0
for b in boards:
  answer += sum(b)

print(answer)
  
