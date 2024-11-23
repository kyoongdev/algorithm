T = int(input())

result = []
for i in range(T):
    A = map(int, input().split())
    result.append(list(A))

for r in result:
    r.sort()
    print(r[7])
