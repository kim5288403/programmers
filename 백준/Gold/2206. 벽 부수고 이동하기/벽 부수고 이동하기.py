from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    queue = deque()
    queue.append([0, 0, 0])

    while queue:
        x, y, w = queue.popleft()

        # 목적지에 도달하였다면 return
        if x == n - 1 and y == m - 1:
            return visited[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고 벽 부수기를 사용하지 않았다면
            if grid[nx][ny] == 1 and w == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append([nx, ny, 1])
            # 다음 이동할 곳이 벽이 아니고 아직 방문을 한번도 하지 않았다면 
            if grid[nx][ny] == 0 and visited[nx][ny][w] == 0:
                visited[nx][ny][w] = visited[x][y][w] + 1
                queue.append([nx, ny, w])

    return -1


n, m = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(n)]

# 3차원 배열 선언
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs())