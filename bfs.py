from collections import deque

def bfs(graph, start, visited):
  queue = deque([start])
  visited[start] = True
  
  while queue:
    index = queue.popleft()
    for node in graph[index]:
      if not visited[node]:
        visited[node] = True
        queue.append(node)


