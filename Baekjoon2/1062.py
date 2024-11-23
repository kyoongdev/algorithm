from itertools import combinations

N, K = map(int, input().split())

souths = []
baseWords = set(["a", "n", "t", "i", "c"])


for i in range(N):
    word = input()[4:-4]
    wordSet = set(word) - baseWords
    target = wordSet.difference(baseWords)

    souths.append(target)

words = set.union(*souths) - baseWords

if K < 5:
    print(0)
    exit()

if len(words) <= K - 5:
    print(N)
    exit()

selectLength = K - 5
maxCount = 0


for combination in combinations(words, selectLength):
    collected = set(combination)
    count = sum(1 for x in souths if x <= collected)
    maxCount = max(maxCount, count)

print(maxCount)
