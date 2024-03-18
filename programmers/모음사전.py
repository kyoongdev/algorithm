# link :https://school.programmers.co.kr/learn/courses/30/lessons/84512


def getCombination(words, maxLength, output, result):
    if len(result) == maxLength:
        return output.append(result)

    for word in words:
        getCombination(words, maxLength, output, result + word)


def solution(word):
    answer = 0
    words = ["A", "E", "I", "O", "U"]
    output = []
    for i in range(1, 6):
        getCombination(words, i, output, "")

    output.sort()
    index = output.index(word)

    return index + 1


"""
A
AA
AAA
AAAA
AAAAA
AAAAE
AAAEE
AAEEE
AEEEE

"""
