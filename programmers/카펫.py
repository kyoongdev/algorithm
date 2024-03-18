# link : https://school.programmers.co.kr/learn/courses/30/lessons/42842

import math


def solution(brown, yellow):
    answer = []
    v = brown + yellow
    for i in range(math.ceil(math.sqrt(v)), v + 1):
        if v % i == 0:
            h = v / i
            b = i * 2 + 2 * (h - 2)
            y = v - b
            if b == brown and y == yellow:
                answer = [i, h]

    return answer
