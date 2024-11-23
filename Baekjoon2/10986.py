n, m = map(int, input().split())
li = list(map(int, input().split()))

a = [0 for _ in range(m)]
b = 0

for i in range(n):
    b += li[i]
    a[b % m] += 1

# print(a)
answer = a[0]

for v in a:
    # print(v, v * (v - 1) // 2)
    answer += v * (v - 1) // 2
print(answer)
