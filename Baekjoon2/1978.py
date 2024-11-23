import math

N = int(input())
arr = list(map(int, input().split()))


def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True

    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False

    return True


count = 0
for a in arr:
    if isPrime(a):
        count += 1

print(count)
