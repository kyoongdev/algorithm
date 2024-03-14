import sys
 
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
 
for x in range(1, n + 1):
  for y in range(1, n + 1):
    if x == y:
      graph[x][y] = 0
      break 
 
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c
 
for k in range(1, n + 1):
  for a in range(1, n + 1):
    for b in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
 
for a in range(1, n + 1):
  for b in range(1, n + 1):
    if graph[a][b] == INF:
      print("INFINITY")
    else:
      print(graph[a][b], end = " ")
    print()