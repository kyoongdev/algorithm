S = input()
T = input()

## A 추가 혹은 B추가 후 뒤집기


def doCalculate(word, act):

    if act == 1:
        return word[:-1]
    else:

        return word[1:][::-1]


def check(word, act):
    if act == 1:
        return len(word) > 0 and word[-1] == "A"
    else:
        return len(word) > 0 and word[0] == "B"


if len(S) == len(T) and S != T:
    print(0)
    exit()

if len(S) > len(T):
    print(0)
    exit()

isOk = False


def dfs(word):

    if S == word:
        return True

    if check(word, 1):
        if dfs(doCalculate(word, 1)):
            return True
    if check(word, 2):
        if dfs(doCalculate(word, 2)):
            return True

    return False


if dfs(T):
    print(1)
else:
    print(0)
