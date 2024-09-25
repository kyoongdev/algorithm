import heapq


def dijkstra(graph, distances, start):
    queue = []
    distances[start] = 0
    heapq.heappush(
        queue,
        [0, start],
    )

    while queue:
        currentW, currentV = heapq.heappop(queue)

        if distances[currentV] < currentW:
            continue

        for newV, newW in graph[currentV]:
            distance = newW + currentW
            if distance < distances[newV]:
                distances[newV] = distance
                heapq.heappush(queue, [distance, newV])


V, E = list(map(int, input().split()))
K = int(input())

graph = [[] for i in range(V + 1)]
distances = [float("inf") for i in range(V + 1)]


for _ in range(E):
    u, v, w = list(map(int, input().split()))

    graph[u].append((v, w))

dijkstra(graph, distances, K)

for idx, d in enumerate(distances):
    if idx == 0:
        continue
    else:
        if d == float("inf"):
            print("INF")
        else:
            print(d)
