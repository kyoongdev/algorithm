# link : https://school.programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations


def solution(relation):
    # answer = 0
    n_row = len(relation)
    n_col = len(relation[0])  # ->runtime error 우려되는 부분

    candidates = []
    for i in range(1, n_col + 1):
        candidates.extend(combinations(range(n_col), i))
    # print(candidates)
    final = []
    for keys in candidates:
        tmp = [tuple([item[key] for key in keys]) for item in relation]

        if len(set(tmp)) == n_row:
            final.append(keys)
    print(final)
    answer = set(final[:])
    print(answer)
    for i in range(len(final)):
        for j in range(i + 1, len(final)):
            if len(final[i]) == len(set(final[i]).intersection(set(final[j]))):
                answer.discard(final[j])
    # relationKeys = [idx for idx,r in enumerate(relation[0])]

    #     possibles = []
    #     for i in range(len(relationKeys)):
    #         combi = combinations(relationKeys,i + 1)
    #         for c in combi:
    #             possibles.append(list(c))

    #     checkLength = len(relation)
    #     oneCandidates = []
    #     candidates = []
    #     notCandidates = []

    #     for possible in possibles:
    #         candidate = []
    #         for re in relation:
    #             candidateSet = []
    #             for idx,r in enumerate(re):
    #                 if idx in possible:
    #                     if len(possible) == 1:
    #                         candidate.append(r)
    #                     else:
    #                         candidateSet.append(r)
    #             if len(possible) != 1:
    #                 candidate.append(candidateSet)

    #         if len(possible) == 1 :
    #             if len(set(candidate)) == checkLength:
    #                 candidates.append(possible)
    #         else:
    #             isPossible = True
    #             for idx,candi in enumerate(candidate):
    #                 if candi in [c for cIdx,c in enumerate(candidate) if idx != cIdx ]:
    #                     isPossible = False

    #             if isPossible and len([x for x in possible if x not in oneCandidates]) == len(possible):
    #                 candidates.append(possible)

    #     # print(candidates)

    #     result = []
    #     for candies in candidates:
    #         if len(candies) == 1:
    #             result.append(candies)
    #             answer += 1
    #             continue
    #         isExists = False
    #         for i in range(1,len(candies)):
    #             combies = combinations(candies,i)

    #             for combi in combies:
    #                 if list(combi) in candidates:
    #                     isExists = True

    #         if not isExists:
    #             result.append(candies)
    #             answer += 1

    # print(result)

    return 0
