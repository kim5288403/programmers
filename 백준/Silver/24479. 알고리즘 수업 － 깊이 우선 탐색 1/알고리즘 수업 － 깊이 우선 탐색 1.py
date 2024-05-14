import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def dfs(r):
    global cnt
    v[r] = cnt
    arr[r].sort()

    for i in arr[r]:
        if v[i] == 0:
            cnt += 1
            dfs(i)

N, M, R = map(int, input().split())
arr = [[] for _ in range(N + 1)]
v = [0] * (N + 1)
cnt = 1

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

dfs(R)

for i in range(1, N + 1):
    print(v[i])

