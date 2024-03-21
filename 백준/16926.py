
from sys import stdin
from collections import deque

N, M, R = map(int, stdin.readline().split())

matrix = []
answer = [[0]*M for _ in range(N)]
deq = deque()

for i in range(N):
    matrix.append(list(stdin.readline().split()))

loops = min(N, M) // 2
for i in range(loops):
    deq.clear()
    deq.extend(matrix[i][i:M-i])
    deq.extend([row[M-i-1] for row in matrix[i+1:N-i-1]])
    deq.extend(matrix[N-i-1][i:M-i][::-1])
    deq.extend([row[i] for row in matrix[i+1:N-i-1]][::-1])
    
    deq.rotate(-R)
    
    for j in range(i, M-i):                 
        answer[i][j] = deq.popleft()
    for j in range(i+1, N-i-1):             
        answer[j][M-i-1] = deq.popleft()
    for j in range(M-i-1, i-1, -1):        
        answer[N-i-1][j] = deq.popleft()  
    for j in range(N-i-2, i, -1):          
        answer[j][i] = deq.popleft()    

for line in answer:
    print(" ".join(line))


# from collections import deque
# import sys
# input = sys.stdin.readline

# N,M,R = list(map(int,input().split()))

# array = []
# for _ in range(N):
#   array.append(list(map(int,input().split())))

# rotateValue = [(1,0),(0,1),(-1,0),(0,-1)]

# def rotate(arr):
#   global N,M
#   newArray = [[0] * M for _ in range(N)]
#   start = deque([(0,0)])
#   current = 0
#   filled = 0
#   count = 0
#   newArray[0][0] = arr[0][1]
#   currentStart=  [0,0]
#   while True:
    
#     x,y = start.popleft()
#     dx,dy = rotateValue[current]
#     nx,ny = x + dx, y + dy
#     count += 1
    
    
#     if filled + 1 == N * M:
#       break
    
#     if  nx == currentStart[0] and ny == currentStart[0] and newArray[nx][ny] != 0:
#       start.append((nx + 1, ny + 1))
#       currentStart =[nx + 1, ny + 1]
#       continue

#     if 0 <= nx < N and 0<= ny < M:
#       if newArray[nx][ny] == 0:
#         newArray[nx][ny] = arr[x][y]
        
#         filled += 1

#         start.append((nx,ny))
#       else:
#         if current == 3:
#           current = 0
#         else:
#           current += 1
#         start.append((x,y))
#     else:
#       if current == 3:
#         current = 0
#       else:
#         current += 1
#       start.append((x,y))
#   return newArray

# for i in range(R % ((M * 2) + (N - 2) * 2)):
#   array = rotate(array)

# for a in array:
#   print(*a)



          

          
        

