from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
answers= []
for _ in range(T):
  N,K = list(map(int,input().split()))

  times = list(map(int,input().split()))

  graph = [[] for _ in range(N + 1)]
  ingress = [0] * (N+1)
  for _ in range(K):
    x,y = list(map(int,input().split()))
    graph[x].append(y)
    ingress[y] += 1
  
  W = int(input())
  queue = deque([])
  dp = [0] * (N + 1)
  for i in range(1,N + 1):
    if ingress[i] == 0:
      queue.append(i)
      dp[i] = times[i-1]

  while queue:
    current = queue.popleft()

    for g in graph[current]:
      ingress[g] -= 1
      dp[g] = max(dp[g],dp[current] + times[g-1] )
      
      if ingress[g] == 0:
        queue.append(g)
  # print(dp)
  answers.append(dp[W])

for a in answers:
  print(a)







  
