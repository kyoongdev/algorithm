N = int(input())
A = list(map(int, input().split()))
methods = list(map(int, input().split()))

plus = methods[0]
minus = methods[1]
multi = methods[2]
div = methods[3]

maxValue = -1000000000
minValue = 1000000000


def solution(index, pl, mi, mu, di, result):
    global maxValue, minValue, A, plus, minus, multi, div

    if index == len(A):
        maxValue = max(result, maxValue)
        minValue = min(result, minValue)

    if pl < plus:
        solution(index + 1, pl + 1, mi, mu, di, result + A[index])

    if mi < minus:
        solution(index + 1, pl, mi + 1, mu, di, result - A[index])

    if mu < multi:
        solution(index + 1, pl, mi, mu + 1, di, result * A[index])

    if di < div:
        if result < 0:
            solution(index + 1, pl, mi, mu, di + 1, -(-result // A[index]))
        else:
            solution(index + 1, pl, mi, mu, di + 1, result // A[index])


solution(1, 0, 0, 0, 0, A[0])

print(maxValue)
print(minValue)
