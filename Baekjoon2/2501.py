N, K = map(int, input().split())


numbs = set()
for i in range(1, N + 1):
    if N % i == 0:

        numbs.add(i)
numbs = list(numbs)
numbs.sort()

# print(numbs, len(numbs))

if len(numbs) == 0 or len(numbs) < K:
    print(0)
else:
    print(numbs[K - 1])
