import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = graph[y][x] + 1
                    q.append((ny, nx))

M, N = map(int, input().split())
graph = [list(map(int, input().strip().split())) for _ in range(N)]
q = deque()
result = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, graph[i][j])

print(result - 1)
