# stringOne = input()
# stringTwo = input()

# N = len(stringOne)
# M = len(stringTwo)

# dp = [[0] * (N + 1) for _ in range(M + 1)]

# for i in range(1, M +1):
#   for j in range(1, N + 1):
#     if stringTwo[i - 1] == stringOne[j - 1]:
#       dp[i][j] = dp[i-1][j-1] + 1
#     else:
#       dp[i][j] = max(dp[i][j-1], dp[i-1][j])

# # print(dp[M][N])

def solution(n, left, right):
    answer = [[1,2,3],[4,5,6],[7,8,9]]
    
    for i in range(left,right+1):

        x = i // n + 1

        y = i % n + 1
        print(x,y, answer[x-1][y-1])
        # if x > y:
        #     arr.append(x)
        # else:
        #     arr.append(y)
        
    return arr

solution(3,2,5)