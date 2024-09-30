word = input()


result = [""] * len(word)


def solution(inputWords, startIdx):
    global result

    if inputWords == "":
        return

    minChar = min(inputWords)
    minCharIdx = inputWords.index(minChar)

    result[startIdx + minCharIdx] = minChar

    print("".join(result))

    solution(inputWords[minCharIdx + 1 :], startIdx + minCharIdx + 1)
    solution(inputWords[:minCharIdx], startIdx)


solution(word, 0)
