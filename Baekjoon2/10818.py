N = int(input())
numbers = map(int, input().split())

minValue = float("inf")
maxValue = -1000000

for numb in numbers:
    minValue = min(numb, minValue)
    maxValue = max(numb, maxValue)

print(minValue, maxValue)
