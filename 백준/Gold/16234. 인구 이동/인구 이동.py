import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def bfs(si, sj):
    q.append((si, sj))
    v[si][sj] = 1
    alst = [(si, sj)]
    amount = arr[si][sj]

    while q:
        ci, cj = q.popleft()

        for i in range(4):
            ni = ci + dy[i]
            nj = cj + dx[i]
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and L <= abs(arr[ci][cj] - arr[ni][nj]) <= R:
                q.append((ni, nj))
                v[ni][nj] = 1
                alst.append((ni, nj))
                amount += arr[ni][nj]

    if len(alst) > 1:
        for ai, aj in alst:
            arr[ai][aj] = amount // len(alst)
        return 1
    return 0


N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
q = deque()
ans = 0
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while ans <= 2000:
    v = [[0] * N for _ in range(N)]
    flag = 0

    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                flag = max(flag, bfs(i, j))
    if flag == 0:
        break
    ans += 1

print(ans)
