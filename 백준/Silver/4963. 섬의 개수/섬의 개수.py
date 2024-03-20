import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(y, x):
    dx = [1, -1, 0, 0, 1, -1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if not visited[ny][nx] and field[ny][nx] == 1:
                visited[ny][nx] = True
                dfs(ny, nx)
while(True):
    w, h = map(int, input().split())

    if w == 0 and h == 0:
        break

    field = [list(map(int, input().strip().split())) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    count = 0

    for i in range(h):
        for j in range(w):
            if not visited[i][j] and field[i][j] == 1:
                visited[i][j] = True
                dfs(i, j)
                count += 1
    print(count)

