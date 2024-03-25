import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    if x == (N - 1) and y == (M - 1):
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    count = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[ny][nx] and graph[y][x] > graph[ny][nx]:
                count += dfs(ny, nx)

    dp[y][x] = count
    return dp[y][x]

M, N = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(M)]
visited = [[False] * N for _ in range(M)]
dp = [[-1] * N for _ in range(M)]
dfs(0, 0)

print(dfs(0,0))
