import re

T = int(input())

answers = []
regex = "^[A-F]?A+F+C+[A-F]?$"
for _ in range(T):
  string = input()

  
  p = re.compile(regex)
  if not p.match(string):
    answers.append("Good")
  else:
    answers.append("Infected!")

for a in answers:
  print(a)



    