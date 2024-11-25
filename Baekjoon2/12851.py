from collections import deque

N, K = map(int, input().split())

visited = [float("inf")] * 100001
queue = deque([(N, 0)])


minMove = float("inf")
acc = 0

while queue:
    current, count = queue.popleft()

    if count > minMove:
        break

    if current == K:
        acc += 1
        minMove = count
        continue

    for nextLoc in [current - 1, current + 1, current * 2]:
        if 0 <= nextLoc <= 100000 and visited[nextLoc] > count:
            visited[nextLoc] = count + 1
            queue.append((nextLoc, count + 1))


print(minMove)
print(acc)
