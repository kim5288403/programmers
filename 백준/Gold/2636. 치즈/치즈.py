import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x):

    if arr[y][x] == 1:
        c_arr.append((y, x))
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < M:
            if not v[ny][nx]:
                v[ny][nx] = True
                dfs(ny, nx)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
count_a = 0

while True:
    count_b = 0
    c_arr = []
    v = [[False] * M for _ in range(N)]
    dfs(0, 0)
    count_a += 1

    for y, x in c_arr:
        count_b += 1
        arr[y][x] = 0

    flag = False
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                flag = True
                break

    if not flag:
        break

print(count_a)
print(count_b)