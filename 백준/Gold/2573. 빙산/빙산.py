from collections import deque
import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x, v):
    q = deque()
    q.append((y, x))
    v[y][x] = True

    while q:
        qy, qx = q.popleft()

        for i in range(4):
            ny, nx = qy + dy[i], qx + dx[i]
            if not v[ny][nx] and arr[ny][nx] > 0:
                q.append((ny, nx))
                v[ny][nx] = True

def solve():

    for year in range(1, N * M * 10):
        a_sub = [[0] * M for _ in range(N)]

        for i in range(N - 1):
            for j in range(M - 1):
                if arr[i][j] == 0:
                    continue
                for d in range(4):
                    ny, nx = i + dy[d], j + dx[d]
                    if arr[ny][nx] == 0:
                        a_sub[i][j] += 1

        for i in range(N - 1):
            for j in range(M - 1):
                if arr[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - a_sub[i][j])

        v = [[False] * M for _ in range(N)]
        count = 0
        for i in range(N - 1):
            for j in range(M - 1):
                if arr[i][j] > 0 and not v[i][j]:
                    bfs(i, j, v)
                    count += 1
                    if count > 1:
                        return year
        if count == 0:
            return 0



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

result = solve()
print(result)