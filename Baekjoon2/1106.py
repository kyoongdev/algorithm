C, N = list(map(int, input().split()))


# C : 명수
# N : 도시의 개수
cities = []


dp = [float("inf")] * (2000 + 1)
dp[0] = 0

for _ in range(N):
    line = list(map(int, input().split()))
    money = line[0]
    people = line[1]

    dp[people] = min(dp[people], money)

# print(dp)
## C명
## cities = [ [홍보 비용 , 고객의 수]]


for i in range(2, 2000 + 1):
    minValue = float("inf")

    for j in range(1, i + 1):
        몫 = i // j
        나머지 = i % j
        if minValue > (dp[j] * 몫 + dp[나머지]):
            minValue = dp[j] * 몫 + dp[나머지]

    dp[i] = min(dp[i], minValue)

print(min(dp[C:]))
