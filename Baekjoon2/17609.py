N = int(input())


def checkIsPalindrome(word):
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return left, right
        left += 1
        right -= 1
    return -1, -1


for _ in range(N):
    word = input()
    left, right = checkIsPalindrome(word)

    if left == -1:
        print(0)
    else:
        print(word, word[left + 1 : right + 1], word[left:right])
        if checkIsPalindrome(word[left + 1 : right + 1]) == (
            -1,
            -1,
        ) or checkIsPalindrome(word[left:right]) == (-1, -1):
            print(1)
        else:
            print(2)
