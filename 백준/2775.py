T = int(input())

cases = []
for _ in range(T):
  k = int(input())
  n = int(input())
  cases.append([k,n])

## k층의 n호
## k층의 n호에는 k-1층의 1호부터 n호까지 사람수의 합만큼 사람들 데려와 살아야함
## 1층의 1호 

dp = [[0] * 15 for _ in range(15)]
dp[0][1] = 1
dp[0][2] = 3
for i in range(3,15):
  dp[0][i] = i + dp[0][i-1]


for k in range(1,15):
  for i in range(1,15):
    dp[k][i] = sum(dp[k - 1][:i + 1] )
  
# for d in dp:
#   print(d)

for t in cases:
  print(dp[t[0] - 1][t[1]])