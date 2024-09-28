from collections import Counter
import sys


def check(alphabets, string):
    for w in string:

        if w not in alphabets or alphabets[w] == 0:
            return False
        else:
            alphabets[w] -= 1
    return True


T = input()
N = int(input())

books = []

for _ in range(N):
    price, title = input().split()

    books.append((int(price), Counter(title)))


answer = sys.maxsize

for i in range(1 << N):

    price = 0
    alphabets = Counter()

    for j in range(N):
        if (i & 1 << j) != 0:
            price += books[j][0]
            alphabets += books[j][1]

    if check(alphabets, T):
        answer = min(answer, price)

print(-1) if answer == sys.maxsize else print(answer)
