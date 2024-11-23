N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, div = map(int, input().split())

minValue = float("inf")
maxValue = float("-inf")


def dfs(idx, current, plus, minus, multi, div):
    global minValue, maxValue

    if idx == N:
        minValue = min(minValue, current)
        maxValue = max(maxValue, current)
        return

    if plus > 0:
        dfs(idx + 1, current + numbers[idx], plus - 1, minus, multi, div)
    if minus > 0:
        dfs(idx + 1, current - numbers[idx], plus, minus - 1, multi, div)
    if multi > 0:
        dfs(idx + 1, current * numbers[idx], plus, minus, multi - 1, div)
    if div > 0:
        if current < 0:
            dfs(idx + 1, -(-current // numbers[idx]), plus, minus, multi, div - 1)
        else:
            dfs(idx + 1, current // numbers[idx], plus, minus, multi, div - 1)


dfs(1, numbers[0], plus, minus, multi, div)

print(maxValue)
print(minValue)
