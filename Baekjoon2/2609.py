N, M = map(int, input().split())

minValue = max(N, M)


maxDiv = 1
minMul = 1

for i in range(1, minValue + 1):

    if N % i == 0 and M % i == 0:
        maxDiv = i


print(maxDiv)
print(int(maxDiv * N / maxDiv * M / maxDiv))
