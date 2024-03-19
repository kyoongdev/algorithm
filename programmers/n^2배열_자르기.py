# link : https://school.programmers.co.kr/learn/courses/30/lessons/87390

"""
12345
22345
33345
44445
55555
123 223 333
1234 1234 1234 1234
1234 2234 3334 4444

12345 22345 33345 44445 555555
"""


def solution(n, left, right):
    answer = []
    arr = []
    currentIndex = 0

    for i in range(left, right + 1):
        # print(i)
        x = i // n + 1
        y = i % n + 1
        if x > y:
            arr.append(x)
        else:
            arr.append(y)

    return arr
