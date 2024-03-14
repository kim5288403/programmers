import sys
input = sys.stdin.readline

count = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    global count
    count += 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and map[ny][nx] == 1:
            visited[ny][nx] = True
            dfs(ny, nx)

N = int(input())
map = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1 and not visited[i][j]:
            count = 0
            visited[i][j] = True
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))

for k in result:
    print(k)
