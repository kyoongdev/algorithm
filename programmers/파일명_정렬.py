# link : https://school.programmers.co.kr/learn/courses/30/lessons/17686


from collections import deque
from functools import cmp_to_key


def sortFile(a, b):

    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    else:
        if int(a[1]) > int(b[1]):
            return 1
        elif int(a[1]) == int(b[1]):
            if a[-1] > b[-1]:
                return 1
            else:
                return -1
        else:
            return -1


def solution(files):
    answer = []
    searchFiles = [f.lower() for f in files]
    result = []
    for idx, file in enumerate(searchFiles):
        head = ""
        number = ""
        tail = ""

        step = "HEAD"
        for f in file:
            if f.isdigit() and step != "TAIL":
                if len(number) == 5:
                    step = "TAIL"
                    tail += f
                else:
                    step = "NUMBER"
                    number += f
            elif step == "HEAD":
                head += f
            else:
                step = "TAIL"
                tail += f

        # print("head : " , head)
        # print("number : ",number)
        # print("tail : ",tail)
        # print("idx : ",idx)
        # print("---")
        result.append([head, number, tail, idx])

    result.sort(key=cmp_to_key(sortFile))

    return [files[x[-1]] for x in result]
