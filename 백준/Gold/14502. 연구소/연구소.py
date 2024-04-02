import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def bfs(tlst):

    for ti, tj in tlst:
        arr[ti][tj] = 1

    q = deque()
    w = [[0] * M for _ in range(N)]
    cnt = CNT - 3
    for vi, vj in virus:
        q.append((vi, vj))
        w[vi][vj] = 1

    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni, nj = ci + dy[i], cj + dx[i]
            if 0 <= ni < N and 0 <= nj < M and w[ni][nj] == 0 and arr[ni][nj] == 0:
                q.append((ni, nj))
                w[ni][nj] = 1
                cnt -= 1

    for ti, tj in tlst:
        arr[ti][tj] = 0

    return cnt

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
virus = []

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            lst.append((i, j))
        elif arr[i][j] == 2:
            virus.append((i, j))

CNT = len(lst)
v = [0] * CNT
ans = 0

for i in range(CNT - 2):
    for j in range(i + 1, CNT - 1):
        for k in range(j + 1, CNT):
            ans = max(ans, bfs([lst[i], lst[j], lst[k]]))


print(ans)

