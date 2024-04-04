import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(s):
    dv[s] = True
    dfs_arr.append(s)

    for i in arr[s]:
        if not dv[i]:
            dfs(i)

def bfs(s):
    q = deque()
    q.append(s)
    bfs_arr.append(s)
    bv[s] = True

    while q:
        qs = q.popleft()

        for i in arr[qs]:
            if not bv[i]:
                bv[i] = True
                q.append(i)
                bfs_arr.append(i)


N, M, V = map(int, input().split())
arr = [[] for _ in range(N + 1)]
dfs_arr = []
bfs_arr = []
dv = [False] * (N + 1)
bv = [False] * (N + 1)


for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N + 1):
    arr[i].sort()


dfs(V)
bfs(V)

print(*dfs_arr)
print(*bfs_arr)