import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(u):
    for i in graph[u]:
        if not visited[i]:
            visited[i] = True
            dfs(i)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
count = 0

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        count += 1

# print(graph)
# print(visited)
print(count)
