import copy

N, M = list(map(int, input().split()))


node = [[] for _ in range(N)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    node[a].append(b)
    node[b].append(a)

answer = 0


def dfs(start, node, stack):
    global answer
    if answer == 1:
        return
    if len(stack) >= 5:
        answer = 1
        return

    for n in node[start]:
        if n not in stack:
            stack.append(n)
            newStack = copy.deepcopy(stack)
            dfs(n, node, newStack)
            stack.pop()


for i in range(N):
    stack = [i]

    dfs(i, node, stack)

    if len(stack) > 1:
        answer = 1
        break

print(answer)
