# link : https://school.programmers.co.kr/learn/courses/30/lessons/92335

import math


def checkIsPrime(n):
    if n == 1 or n == 0:
        return False
    for t in range(2, math.floor(math.sqrt(n)) + 1):
        if n % t == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    result = []
    value = n

    while n >= k:
        value = n % k
        n = n // k
        result.append(str(value))
    result.append(str(n))
    result.reverse()
    target = "".join(result)
    splitted = target.split("0")

    for s in splitted:
        if len(s) > 0 and checkIsPrime(int(s)):
            answer += 1

    return answer
