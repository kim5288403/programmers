import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(y, x):
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[ny][nx] and graph[ny][nx] == 0:
                visited[ny][nx] = True
                count += 1
                dfs(ny, nx)

    return count

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]
count = 1
call_cnt = 0
sum_list = []

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 0:
            visited[i][j] = True
            call_cnt += 1
            sum_list.append(dfs(i, j))
            count = 1

sum_list.sort()
result_string = ' '.join(map(str, sum_list))

print(call_cnt)
print(result_string)
