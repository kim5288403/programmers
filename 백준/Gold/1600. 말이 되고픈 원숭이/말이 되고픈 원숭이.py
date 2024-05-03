import sys
from collections import deque
input = sys.stdin.readline
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
hdx = [-2, -2, -1, -1, 2, 2, 1, 1]
hdy = [-1, 1, -2, 2, -1, 1, -2, 2]

def bfs():
    q = deque()
    q.append((0, 0, 0))
    v[0][0][0] = 1

    while q:
        x, y, z = q.popleft()
        if x == (H - 1) and y == (W - 1):
            return v[x][y][z] - 1

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < H and 0 <= ny < W:
                if not v[nx][ny][z] and not arr[nx][ny]:
                    v[nx][ny][z] = v[x][y][z] + 1
                    q.append((nx, ny, z))

        if z < K:
            for i in range(8):
                hnx = x + hdx[i]
                hny = y + hdy[i]
                if 0 <= hnx < H and 0 <= hny < W:
                    if not arr[hnx][hny]:
                        if not v[hnx][hny][z + 1]:
                            v[hnx][hny][z + 1] = v[x][y][z] + 1
                            q.append((hnx, hny, z + 1))

    return -1


K = int(input())
W, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(H)]
v = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]

print(bfs())


