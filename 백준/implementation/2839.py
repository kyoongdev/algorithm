import math

n = int(input())
count = 0
while n > 0:
  if n % 5 != 0:
    n -= 3
    count += 1
  else:
    n -= 5
    count += 1
    
if n < 0:
  print(-1)
else:
  print(count)
