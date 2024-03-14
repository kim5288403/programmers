import sys
sys.setrecursionlimit(10000)

def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N:
            if field[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                dfs(ny, nx)


for _ in range(int(sys.stdin.readline())):
    M, N, K = map(int, sys.stdin.readline().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1

    for x in range(M):
        for y in range(N):
            if field[y][x] == 1 and not visited[y][x]:
                visited[y][x] = True
                dfs(y, x)
                count += 1

    print(count)



