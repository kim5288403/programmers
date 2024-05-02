import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j):
    if dp[i][j]:
        return dp[i][j]

    dp[i][j] = 1

    for k in range(4):
        ni = di[k] + i
        nj = dj[k] + j
        if 0 <= ni < N and 0 <= nj < N and arr[i][j] < arr[ni][nj]:
            dp[i][j] = max(dp[i][j], dfs(ni, nj) + 1)
    return dp[i][j]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        result = max(result, dfs(i, j))
print(result)
