# link : https://school.programmers.co.kr/learn/courses/30/lessons/17677


from collections import deque
import math

"""
자카드 유사도 = 교집합 원소 수 / 합집합 원소 수 , 둘 다 공집합 -> 1
"""


def solution(str1, str2):
    answer = 0
    str1 = [s.lower() for s in str1]
    str2 = [s.lower() for s in str2]

    str1 = deque(str1)
    str2 = deque(str2)
    str1Dict = {}
    str2Dict = {}

    str1Word = ""
    str2Word = ""
    while str1:
        one = str1.popleft()
        if one.isalpha():

            str1Word += one
            if len(str1Word) == 2:
                if str1Word in str1Dict:
                    str1Dict[str1Word] += 1
                else:
                    str1Dict[str1Word] = 1
                str1Word = one
        else:
            str1Word = ""
    # if len(str1Word) > 0:
    #     if str1Word in str1Dict:
    #         str1Dict[str1Word] += 1
    #     else:
    #         str1Dict[str1Word] = 1
    while str2:
        two = str2.popleft()
        if two.isalpha():
            str2Word += two
            if len(str2Word) == 2:
                if str2Word in str2Dict:
                    str2Dict[str2Word] += 1
                else:
                    str2Dict[str2Word] = 1
                str2Word = two
        else:
            str2Word = ""

    # if len(str2Word) > 0:
    #     if str2Word in str2Dict:
    #         str2Dict[str2Word] += 1
    #     else:
    #         str2Dict[str2Word] = 1

    # print("str1Dict",str1Dict)
    # print("str2Dict", str2Dict)

    if len(str1Dict.keys()) == 0 and len(str2Dict.keys()) == 0:
        return 65536

    # 교집합
    together = 0
    # 합집합
    union = 0

    for keyOne, valueOne in str1Dict.items():
        if str2Dict.get(keyOne):
            if valueOne == str2Dict[keyOne]:
                together += valueOne
                union += valueOne
            else:
                together += min(valueOne, str2Dict[keyOne])
                union += max(valueOne, str2Dict[keyOne])
            del str2Dict[keyOne]
        else:
            union += valueOne

    # print("str1Dict",str1Dict)
    # print("str2Dict", str2Dict)
    for keyTwo, valueTwo in str2Dict.items():
        union += valueTwo

    # print(together,union)

    answer = math.floor((together / union) * 65536)

    return answer
