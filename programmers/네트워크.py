# link : https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque


def solution(n, computers):
    answer = 0
    visited = [False] * n
    graph = []
    cpQueue = deque(computers)
    for cpIdx, cp in enumerate(computers):
        node = []
        for ctIdx, ct in enumerate(cp):
            if cpIdx != ctIdx and ct == 1:
                node.append(ctIdx)
        graph.append(node)

    def dfs(nodes, visited, startNode):
        visited[startNode] = True

        for node in nodes[startNode]:
            if not visited[node]:
                dfs(nodes, visited, node)

    connections = []

    for i in range(n):
        visited = [False] * n
        dfs(graph, visited, i)
        groups = [idx for idx, x in enumerate(visited) if x]
        groups.sort()
        groupTuple = tuple(groups)
        if groupTuple not in connections:
            connections.append(groupTuple)

    return len(connections)
