
from collections import deque

def bfs(graph,start,visited):
    queue = deque([start])

    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



def dfs(nodes, idx ,visited):
    visited[idx] = True
    print("idx",idx)
    for node in nodes[idx]:
        if not visited[node]:
            dfs(nodes,node,visited)

