N = int(input())

numbers = list(map(int,input().split(" ")))

dp = [0] * N
dp[0] = numbers[0]
for i in range(1,N):
  dp[i] = max(dp[i-1] + numbers[i], numbers[i])

print(max(dp))


# dp = [[0] * N for _ in range(N)]

# dp[0][0] = numbers[0]

# for i in range(1,N):
#   dp[0][i] = numbers[i] + dp[0][i-1]

# for i in range(1,N):
#   for j in range(i,N):
#     dp[i][j] = dp[0][j] - dp[0][i-1] 

# print(max(*[max(x[idx:])for idx,x in enumerate(dp)]))

