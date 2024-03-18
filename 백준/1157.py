from collections import Counter

alpha = input().upper()

alphaDict= {}
for a in alpha:
  if a in alphaDict:
    alphaDict[a] += 1
  else:
    alphaDict[a] = 1

common = Counter(alphaDict).most_common()

if len(common) == 1:
  x,y =common[0]
  print(x)
else:
  fs,fc = common[0]
  ss,sc = common[1]
  if fc == sc:
    print("?")
  else:
    print(fs)

