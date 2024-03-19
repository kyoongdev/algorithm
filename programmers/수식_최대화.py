# link : https://school.programmers.co.kr/learn/courses/30/lessons/67257


from collections import deque
from itertools import permutations


def calc(method, first, second):
    if method == "+":
        return int(first) + int(second)
    elif method == "-":
        return int(first) - int(second)
    else:
        return int(first) * int(second)


def solution(expression):
    answer = 0
    eq = deque([e for e in expression])
    sumi = ""
    expressions = []
    while eq:
        e = eq.popleft()
        if e.isdigit():
            sumi += e
        else:
            expressions.append(sumi)
            expressions.append(e)
            sumi = ""
    expressions.append(sumi)
    priority = list(permutations(["-", "+", "*"], 3))
    # print(priority)
    # print(expressions)

    for p in priority:
        first, second, third = p

        exp = expressions.copy()

        while first in exp:
            fIdx = exp.index(first)
            before = exp[fIdx - 1]

            after = exp[fIdx + 1]
            result = calc(first, before, after)
            beforeExp = exp[: fIdx - 1]
            afterExp = exp[fIdx + 2 :]
            exp = [*beforeExp, str(result), *afterExp]

        while second in exp:
            fIdx = exp.index(second)
            before = exp[fIdx - 1]

            after = exp[fIdx + 1]
            result = calc(second, before, after)
            beforeExp = exp[: fIdx - 1]
            afterExp = exp[fIdx + 2 :]
            exp = [*beforeExp, str(result), *afterExp]

        while third in exp:
            fIdx = exp.index(third)
            before = exp[fIdx - 1]

            after = exp[fIdx + 1]
            result = calc(third, before, after)
            beforeExp = exp[: fIdx - 1]
            afterExp = exp[fIdx + 2 :]
            exp = [*beforeExp, str(result), *afterExp]

        if answer < abs(int(exp[0])):
            answer = abs(int(exp[0]))

    return answer
