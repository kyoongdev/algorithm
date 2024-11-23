s = int(input())

if s == 1:
    print(1)
    exit(0)

sum = 0
count = 0
for count in range(1, s + 1):
    sum += count

    if sum > s:
        break

print(count - 1)
