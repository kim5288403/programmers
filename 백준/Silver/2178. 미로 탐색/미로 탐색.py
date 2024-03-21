import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(y, x):

    while q:
        qy, qx = q.popleft()
        for i in range(4):
            nx = qx + dx[i]
            ny = qy + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if visited[ny][nx] == 0 and field[ny][nx] == 1:
                    visited[ny][nx] = visited[qy][qx] + 1
                    q.append((ny, nx))


N, M = map(int, input().split())
field = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
q = deque()

q.append((0, 0))
bfs(0, 0)

print(visited[N - 1][M - 1] + 1)