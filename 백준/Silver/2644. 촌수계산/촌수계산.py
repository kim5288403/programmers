import sys

def dfs(x, count):
    global flag
    visited[x] = True

    if x == C:
        print(count)

    for i in graph[x]:
        if not visited[i]:
            dfs(i, count + 1)

N = int(input())
P, C = map(int, input().split())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(P, 0)
if not visited[C]:
    print(-1)
