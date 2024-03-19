N = int(input())

numbers = list(map(int, input().split()))
reversedNumbers = numbers[::-1]

dpUp = [1] * N
dpDown = [1] * N

for i in range(N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dpUp[i] = max(dpUp[i], dpUp[j] + 1)
        if reversedNumbers[i] > reversedNumbers[j]:
            dpDown[i] = max(dpDown[i], dpDown[j] + 1)

result = [0] * N
for i in range(N):
    result[i] = dpUp[i] + dpDown[N - i - 1] - 1

print(max(result))
