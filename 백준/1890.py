N = int(input())


board = []

for _ in range(N):
  board.append(list(map(int,input().split(" "))))

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
## 각 칸에 도착할 수 있는 최소의 경우의 수를 저장

for x in range(N):
  for y in range(N):
    if x == N - 1 and y == N -1:
      continue
    jump = board[x][y]

    if N > x + jump:
      dp[x + jump][y] += dp[x][y]
    if N > y + jump:
      dp[x][y + jump] += dp[x][y]

    
print(dp[N-1])