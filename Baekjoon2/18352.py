import heapq

N, M, K, X = list(map(int, input().split()))


nodes = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = list(map(int, input().split()))

    nodes[A].append([B, 1])


def dijkstra(graph, start):
    distances = [float("inf") for node in graph]

    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        currentDistance, currentDestination = heapq.heappop(queue)

        if distances[currentDestination] < currentDistance:
            continue

        for newDestination, newDistance in graph[currentDestination]:
            distance = currentDistance + newDistance
            if distance < distances[newDestination]:
                distances[newDestination] = distance
                heapq.heappush(queue, [distance, newDestination])

    return distances


distances = dijkstra(nodes, X)


result = []

for node, distance in enumerate(distances):
    if distance == K:
        result.append(node)


result.sort()

if len(result) == 0:
    print(-1)
else:
    for r in result:
        print(r)
