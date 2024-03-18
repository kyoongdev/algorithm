N = input()


if len(N) == 1:
  N = "0" + N

cycle = 0
savedN = N
while True:
  
  new = str(int(N[0]) + int(N[1]))
  
  new = N[-1] +new[-1]
  cycle += 1
  if new == savedN:
    break
  else:
    N = new
    
print(cycle)




