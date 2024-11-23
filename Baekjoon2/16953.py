A, B = map(int, input().split())

count = float("inf")


def dfs(number, acc):
    global B, count
    if number > B:
        return

    if number == B:
        count = min(count, acc)
        return

    dfs(number * 2, acc + 1)
    dfs(int(str(number) + "1"), acc + 1)


dfs(A, 1)

if count == float("inf"):
    print(-1)
else:

    print(count)
