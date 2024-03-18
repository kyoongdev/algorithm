import math
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
  numbers.append(int(input()))
numbers.sort()

## 평균값
avg = round(sum(numbers) / N)
print(avg)

## 중앙값
middle = numbers[N // 2]
print(middle)

maxCount = -1
maxNumbers = []
numberCount = 0
for number,count in Counter(numbers).most_common():
  if count >= maxCount:
    maxCount = count
    numberCount += 1
    maxNumbers.append(number)
  else:
    break

if numberCount > 1:
  print(maxNumbers[1])
else:
  print(maxNumbers[0])

print(numbers[-1] - numbers[0])