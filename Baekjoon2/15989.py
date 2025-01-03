T = int(input())

cases = []

for _ in range(T):
    cases.append(int(input()))


dp = [1] * (max(cases) + 1)

for i in range(2, 4):
    for j in range(1, max(cases) + 1):
        if i <= j:
            dp[j] = dp[j] + dp[j - i]

for c in cases:
    print(dp[c])

"""
1 : 1
2 : 1 + 1, 2 => 2
3 : 1 + 1 + 1, 2 + 1, 3 = >3
4 : 1 + 1 + 1 + 1, 2 + 1 + 1, 3 + 1, 2 + 2
5 : 1 *5, 
"""
