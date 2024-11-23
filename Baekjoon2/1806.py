N, S = map(int, input().split())

numbers = list(map(int, input().split()))

dp = [0] * (N + 1)

for i in range(1, N + 1):
    dp[i] = dp[i - 1] + numbers[i - 1]


start = 0
end = 1
answer = float("inf")


while start < N:

    if dp[end] - dp[start] >= S:
        answer = min(answer, end - start)
        start += 1
    else:
        if end <= N - 1:
            end += 1
        else:
            start += 1

if answer == float("inf"):
    print(0)
else:
    print(answer)
