import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(root):

    for i in graph[root]:
        if visited[i] == 0:
            visited[i] = root
            dfs(i)


N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)

for i in range(2, len(visited)):
    print(visited[i])