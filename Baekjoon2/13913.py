from collections import deque

N, K = map(int, input().split())

queue = deque([(N, 0, f"{N}")])
visited = [float("inf")] * 100_001
result = 0
accResult = ""

while queue:
    current, count, acc = queue.popleft()

    if current == K:
        result = count
        accResult = acc
        break

    for nextPos in [current - 1, current + 1, current * 2]:
        if 0 <= nextPos <= 100000 and visited[nextPos] > count:
            visited[nextPos] = count

            queue.append((nextPos, count + 1, f"{acc} {nextPos}"))

print(result)
print(accResult)
