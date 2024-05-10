import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j):
    global count

    for l in range(4):
        ni = di[l] + i
        nj = dj[l] + j
        if 0 <= ni < N and 0 <= nj < M:
            if not v[ni][nj] and arr[ni][nj] == "#":
                v[ni][nj] = True
                count += 1
                dfs(ni, nj)

    return count

N, M, K = map(int, input().split())
arr = [["."] * M for _ in range(N)]
v = [[False] * M for _ in range(N)]
result = 0

for i in range(K):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = "#"

for i in range(N):
    for j in range(M):
        if not v[i][j] and arr[i][j] == "#":
            count = 1
            v[i][j] = True
            result = max(result, dfs(i, j))


print(result)
