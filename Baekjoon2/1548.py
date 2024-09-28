N = int(input())
numbs = sorted(list(map(int, input().split())))

if N == 1:
    print(N)
    exit()

answer = 2

for i in range(1, N):

    for start in range(0, i):
        end = start + 2
        while end < N:
            if numbs[start] + numbs[start + 1] > numbs[end]:
                answer = max(answer, end - start + 1)
            end += 1


print(answer)
