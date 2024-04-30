import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

def dfs(i, j):
    for k in range(4):
        ni = di[k] + i
        nj = dj[k] + j
        if 0 <= ni < N and 0 <= nj < M:
            if arr[ni][nj] >= 1:
                arr[ni][nj] += 1
            elif not v[ni][nj] and arr[ni][nj] == 0:
                v[ni][nj] = True
                dfs(ni, nj)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count = 0
flag = True

while flag:
    count += 1
    v = [[False] * M for _ in range(N)]
    dfs(0, 0)

    for i in range(N):
        for j in range(M):
            if arr[i][j] > 2:
                arr[i][j] = 0
            elif arr[i][j] > 0:
                arr[i][j] = 1

    flag = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                flag = True
                break

print(count)
