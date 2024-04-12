import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    global count_b

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= nx < M and 0 <= ny < N:
            if not v[ny][nx] and arr[ny][nx] == 1:
                v[ny][nx] = True
                count_b += 1
                dfs(ny, nx)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
v = [[False] * M for _ in range(N)]

result = 0
count_a = 0
count_b = 0


for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and not v[i][j]:
            v[i][j] = True
            count_b = 1
            dfs(i, j)
            result = max(result, count_b)
            count_a += 1

print(count_a)
print(result)
