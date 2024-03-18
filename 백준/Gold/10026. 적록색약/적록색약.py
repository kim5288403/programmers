import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[ny][nx] and field[y][x] == field[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx)


N = int(input())
field = [list(input().strip()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
countA = 0
countB = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            countA += 1

visited = [[False] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if field[i][j] == "G":
            field[i][j] = "R"

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(i, j)
            countB += 1

print(countA, countB)



