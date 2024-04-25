import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(s, depth):
    global flag
    v[s] = True

    if depth == 5:
        flag = True
        return

    for x in arr[s]:
        if not v[x]:
            v[x] = True
            dfs(x, depth + 1)
            v[x] = False

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
v = [False] * N
flag = False

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(N):
    dfs(i, 1)
    v[i] = False
    if flag:
        break

if flag:
    print(1)
else:
    print(0)
