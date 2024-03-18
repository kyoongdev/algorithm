#link : https://school.programmers.co.kr/learn/courses/30/lessons/42579

"""
가장 많이 재생된 노래 2개씩 베스트 앨범

속한 노래가 많이 재생된 장르 먼저 수록
장르 내에서 많이 재생된 노래 수록
장르 내에서 재생 횟수가 같은 노래 -> 고유번호 낮은 거 수록
"""
from collections import Counter
from collections import defaultdict
from functools import cmp_to_key


def sortPlay(a,b):
    if a[0] > b[0]:
        return -1
    elif a[0] == b[0]:
        if a[1] > b[1]:
            return 1
        else:
            return -1
    else:
        return 1
        
def solution(genres, plays):
    answer = []
    playCountDict = {}
    genrePlayDict = defaultdict(list)
    for idx,(genre,play) in enumerate(zip(genres,plays)):
        if genre in playCountDict:
            playCountDict[genre] += play
        else:
            playCountDict[genre] = play
        genrePlayDict[genre].append([play,idx])
        
    for gk in genrePlayDict.keys():
        genrePlayDict[gk].sort(key=cmp_to_key(sortPlay))
            
            
    most = Counter(playCountDict).most_common()
    for m in most:
        genre,play = m
        count = 0
        for p in genrePlayDict[genre]:
            answer.append(p[1])
            count += 1
            if count == 2:
                break
            
    return answer