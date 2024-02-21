def dfs(graph,start,visited):
  visited[start] = True

  for node in graph[start]:
    if not visited[node]:
      visited[node] = True
      dfs(graph, node, visited)