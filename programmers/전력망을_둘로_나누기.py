# link : https://school.programmers.co.kr/learn/courses/30/lessons/86971


from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    # print(start,visited)
    visited[start] = True
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


def solution(n, wires):

    maxDiff = n
    for idx, wire in enumerate(wires):
        graph = [[] for i in range(n + 1)]
        tmpWires = wires.copy()
        tmpWires.pop(idx)
        visited = [False] * (n + 1)

        for wire in tmpWires:
            graph[wire[0]].append(wire[1])
            graph[wire[1]].append(wire[0])

        bfs(graph, 1, visited)

        trueCount = visited.count(True)
        groupOne = trueCount
        groupTwo = n - trueCount
        diffAbs = abs(groupOne - groupTwo)

        if diffAbs < maxDiff:
            maxDiff = diffAbs

    return maxDiff
