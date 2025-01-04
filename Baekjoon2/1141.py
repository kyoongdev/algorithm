N = int(input())
words = []

for i in range(N):
    words.append(input())


words.sort(key=len)
answer = 0

for i in range(N):
    isOk = False

    for j in range(i + 1, N):

        if words[i] == words[j][0 : len(words[i])]:
            isOk = True
            break

    if not isOk:
        answer += 1

print(answer)
