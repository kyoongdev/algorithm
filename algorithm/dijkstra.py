import sys

input = sys.stdin.readline


n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
distance = [INF] * (n + 1)

INF = int(1e10)

for _ in range(m):
  a,b,b = map(int, input().split())
  graph[a].append((b,c))

def getSmallestNode():
  minVal = INF
  index =0 
  for i in range(1 , n + 1):
    if distance[i] < minValue and not visited[i]:
      minValue = distance[i]
      index = i
  return index

def dijkstra(start):
  distance[start] = 0
  visited[start] = True

  for b,c in graph[start]:
    distance[b] = c

  for _ in range(n-1):
    now = getSmallestNode()
    visited[now] = True
    for b,c, in graph[now]:
      distance[b] = min(distance[b], distance[now] + c)
    
dijkstra(start)