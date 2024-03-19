# link : https://school.programmers.co.kr/learn/courses/30/lessons/60058

from collections import deque


def checkIsBalanced(word):
    openCount = word.count("(")
    closeCount = word.count(")")
    return openCount == closeCount


def checkIsComplete(word):
    if len(word) == 0 or word[0] == ")" or word[-1] == "(" or not checkIsBalanced(word):
        return False
    queue = deque([x for x in word])
    openCount = 0
    closeCount = 0
    isClosed = False
    while queue:
        q = queue.popleft()
        if q == "(":
            openCount += 1
            isClosed = False
        else:
            if openCount == 0 and closeCount == 0:
                return False
            closeCount += 1
            if openCount == closeCount:
                isClosed = True
                openCount = 0
                closeCount = 0
    return isClosed and openCount == closeCount


def seperateWord(word):
    u = ""
    v = ""
    for idx, l in enumerate(word):
        if (
            idx != 0
            and checkIsBalanced(word[: idx + 1])
            and checkIsBalanced(word[idx + 1 :])
        ):
            u = word[: idx + 1]
            v = word[idx + 1 :]
            break
    return u, v


def solution(p):
    answer = ""

    if len(p) == 0:
        return ""
    if checkIsComplete(p):
        return p

    def getSeperatedWord(word):

        if len(word) == 0:
            return ""
        u, v = seperateWord(word)

        # print("u : ",u,checkIsComplete(u))
        # print("v : ",v)
        if checkIsComplete(u):
            return u + getSeperatedWord(v)
        else:
            u = u[1:-1]
            newValue = ""
            for i in u:
                if i == "(":
                    newValue += ")"
                else:
                    newValue += "("
            # print("getSeperatedWord",getSeperatedWord(v),"newValue",newValue)
            return "(" + getSeperatedWord(v) + ")" + newValue

    return getSeperatedWord(p)
