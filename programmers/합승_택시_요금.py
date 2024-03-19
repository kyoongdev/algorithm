# link : https://school.programmers.co.kr/learn/courses/30/lessons/72413
INF = int(1e9)


def solution(n, s, a, b, fares):
    answer = 0

    graph = [[] for _ in range(n)]

    for fare in fares:
        graph[fare[0] - 1].append([fare[1] - 1, fare[2]])
        graph[fare[1] - 1].append([fare[0] - 1, fare[2]])
    print(graph)

    def getSmallestNode(nodes, visited):
        minValue = INF
        index = -1

        for i in range(len(nodes)):
            if not visited[i] and minValue > nodes[i]:
                minValue = nodes[i]
                index = i
        return index

    def dijkstra(startNode):
        nonlocal n, graph
        nodes = [INF] * n
        visited = [False] * n

        visited[startNode] = True
        nodes[startNode] = 0
        print(graph[startNode])
        for node in graph[startNode]:
            nodes[node[0]] = min(nodes[node[0]], node[1])

        for i in range(n):
            now = getSmallestNode(nodes, visited)
            visited[now] = True
            for node in graph[now]:
                nodes[node[0]] = min(nodes[node[0]], nodes[now] + node[1])

        return nodes

    graphA = dijkstra(a - 1)
    graphB = dijkstra(b - 1)
    graphS = dijkstra(s - 1)

    answer = INF
    for i in range(n):
        value = graphA[i] + graphB[i] + graphS[i]
        if value < answer:
            answer = value

    #     graph = [[INF] * (n) for _ in range(n)]

    #     for x in range(n):
    #         for y in range(n):
    #             if x == y:
    #                 graph[x][y] = 0

    #     for fare in fares:
    #         graph[fare[0] - 1][fare[1] - 1] = fare[-1]
    #         graph[fare[1] - 1][fare[0] - 1] = fare[-1]

    #     # for g in graph:
    #     #     print(g)

    #     for i in range(n):
    #         for j in range(n):
    #             for k in range(n):
    #                 graph[j][k] = min(graph[j][k], graph[j][i] + graph[i][k] )

    #     answer = graph[s - 1][a - 1] + graph[s - 1][b - 1]

    #     for i in range(n):
    #         answer = min(answer, graph[s - 1][i] + graph[i][a-1] + graph[i][b-1])

    return answer
