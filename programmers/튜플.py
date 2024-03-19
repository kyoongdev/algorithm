# link : https://school.programmers.co.kr/learn/courses/30/lessons/64065


from functools import cmp_to_key


def sort(a, b):
    if len(a) > len(b):
        return 1
    else:
        return -1


def solution(s):
    answer = []
    total = []

    parsedS = [
        x[1:] if x[0] == "," else x for x in s.replace("{", "").split("}") if len(x) > 0
    ]
    parsedS.sort(key=cmp_to_key(sort))

    for ps in parsedS:
        splitted = ps.split(",")
        for sp in splitted:
            if int(sp) not in total:
                total.append(int(sp))

    return total
