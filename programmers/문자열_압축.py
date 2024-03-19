# link : https://school.programmers.co.kr/learn/courses/30/lessons/60057

from collections import deque

"""
ab ab cd cd ab ab cd cd

abc abc ded e
"""


def getLength(word):
    if len(word) > 1:
        return str(len(word))
    else:
        return ""


def solution(s):
    answer = 0
    minLength = len(s)

    def getWord(word, n):
        queue = deque([])
        for i in range(0, len(word), n):
            queue.append(word[i if i != 0 else 0 : i + n if i + n != n else n])
        poppedWords = []
        result = ""
        while queue:
            q = queue[0]
            if len(queue) == 1:
                if len(poppedWords) == 0:
                    result += q
                elif poppedWords[0] == q:
                    result += getLength([*poppedWords, q]) + poppedWords[0]
                else:
                    result += getLength(poppedWords) + poppedWords[0]
                    result += q
            elif len(poppedWords) == 0:
                poppedWords.append(q)
            elif poppedWords[0] == q:
                poppedWords.append(q)
            elif poppedWords[0] != q:
                result += getLength(poppedWords) + poppedWords[0]
                poppedWords = [q]
            queue.popleft()

        return len(result)

    for i in range(1, len(s) // 2 + 1):
        count = getWord(s, i)

        if count < minLength:
            minLength = count

    return minLength
