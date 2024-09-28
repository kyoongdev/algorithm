H, W = list(map(int, input().split()))

blocks = list(map(int, input().split()))

rains = 0


for i in range(1, W - 1):
    leftHeight = max(blocks[:i])
    rightHeight = max(blocks[i + 1 :])

    minHeight = min(leftHeight, rightHeight)
    if minHeight > blocks[i]:
        rains += minHeight - blocks[i]


print(rains)


"""
4 12
0 1 0 1 4 1 2 1 1 1 1 4
"""
