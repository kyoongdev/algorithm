string = list(input())
stack = []

tmp = 1
answer = 0

for idx, s in enumerate(string):
    if s == "(":
        stack.append(s)
        tmp *= 2
    elif s == "[":
        stack.append(s)
        tmp *= 3
    elif s == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if string[idx - 1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2
    elif s == "]":
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if string[idx - 1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
