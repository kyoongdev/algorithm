from collections import deque
import sys

input = sys.stdin.readline


answer = []
for _ in range(int(input())):
    N, K = list(map(int, input().split()))

    times = list(map(int, input().split()))
    dp = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    result = []
    for _ in range(K):
        x, y = tuple(map(int, input().split()))
        graph[x].append(y)
        indegree[y] += 1

    W = int(input())
    queue = deque([])
    for i in range(1, N + 1):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = times[i - 1]

    while queue:
        value = queue.popleft()
        result.append(value)
        for i in graph[value]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[value] + times[i - 1])
            if indegree[i] == 0:
                queue.append(i)
    # print(dp)
    answer.append(dp[W])

for a in answer:
    print(a)
