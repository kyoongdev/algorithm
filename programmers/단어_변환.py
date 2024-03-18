# link :https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque


def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    def checkWordDiff(word, targetWord):
        count = 0
        for idx, w in enumerate(word):
            if w != targetWord[idx]:
                count += 1
        return count

    queue = deque([(begin, 0)])
    visited = [False] * len(words)
    while queue:
        q, cnt = queue.popleft()
        if q == target:
            answer = cnt
            break

        for idx, word in enumerate(words):
            if not visited[idx] and checkWordDiff(q, word) == 1:
                visited[idx] = True
                queue.append((word, cnt + 1))

    return answer
