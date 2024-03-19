import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(y, x, k):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if not visited[ny][nx] and field[ny][nx] > k:
                visited[ny][nx] = True
                dfs(ny, nx, k)

N = int(input())
field = [list(map(int, input().strip().split())) for _ in range(N)]
result = 0
max_value = 0
count = 0

for row in field:
    for value in row:
        if value > max_value:
            max_value = value

for k in range(max_value):
    visited = [[False] * N for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and field[i][j] > k:
                visited[i][j] = True
                dfs(i, j, k)
                count += 1

    result = max(result, count)

print(result)
