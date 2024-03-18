import sys
from bisect import bisect_left
input = sys.stdin.readline
N,M,B = list(map(int,input().split()))

HIGH = 2
LOW = 1

ground = []
groundDict = {}

for _ in range(N):
  tmp = list(map(int,input().split()))
  for t in tmp:
    if t in groundDict:
      groundDict[t] += 1
    else:
      groundDict[t] = 1
  ground.extend(tmp)

answers = []
minTime = 1e10
maxHeight = 0
minG = min(ground)
maxG = max(ground)

keys = list(groundDict.keys())
keys.sort()

# print(groundDict)
for key in range(minG, maxG + 1):
  b = B
  time = 0

  idx = bisect_left(keys,key)
  for h in keys[idx:]:

    time += (h - key) * HIGH * groundDict[h]
    b += (h - key) * groundDict[h]
  
  for l in keys[:idx]:
    time += (key - l) * LOW * groundDict[l]
    b -= (key - l) * groundDict[l]
  # print(key,time,b,idx,keys[:idx])

  if b >= 0 :
    if time < minTime:
      answers = []
      answers.append([time,key])
      minTime = time
    elif time == minTime:

      answers.append([time,key])
    
  
answers.sort()
# print(answers)

print(answers[-1][0],answers[-1][1])
  


"""
각 블록 높이 별로 고르게 하기

1. 해당 블록보다 높은 블럭이 있으면 깎기
2. 해당 블록보다 낮은 블럭이 있으면 올리기
3. 낲은 블록의 수가 음수면 진행 X

"""

"""
블록 제거 후 인벤토리 삽입 -> 2초
인벤토리에서 블록 꺼내서 쌓기 -> 1초
"""
"""
3 4 0
64 64 64 64
64 64 64 65
64 64 64 63

3 64
"""
"""
땅을 쌓거나, 깎거나
"""