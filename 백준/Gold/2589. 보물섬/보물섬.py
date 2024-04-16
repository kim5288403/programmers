from collections import deque
import sys
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def bfs(y, x):
    global result
    q.append((y, x))
    v[y][x] = 1

    while q:
        qy, qx = q.popleft()

        for i in range(4):
            ny, nx = qy + dy[i], qx + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if arr[ny][nx] == "L" and v[ny][nx] == 0:
                    v[ny][nx] = v[qy][qx] + 1
                    result = max(result, v[ny][nx])
                    q.append((ny, nx))

    return result


N, M = map(int, input().split())
arr = [list(input().strip()) for _ in range(N)]
result = 0
q = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == "L":
            v = [[0] * M for _ in range(N)]
            bfs(i, j)

print(result - 1)