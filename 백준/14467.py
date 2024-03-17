from collections import defaultdict

N = int(input())

cowDict=  defaultdict(list)
for _ in range(N):
  cow = list(map(int,input().split(" ")))
  cowDict[cow[0]].append(cow[-1])
# 
# print(cowDict)

answer  = 0
for items in cowDict.values():
  current = items[0]
  count = 0
  # print(items)
  for cross in items[1:]:
    # print("info",cross,current)
    if cross != current:
      current = cross
      count += 1
  answer += count

print(answer)

