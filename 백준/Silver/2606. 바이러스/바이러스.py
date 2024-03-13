import sys

count = 0
def dfs(c):
    global count
    for i in network[c]:
        if not visited[i]:
            visited[i] = True
            dfs(i)
            count += 1


N = int(input())
link = int(input())

network = [[] * (N + 1) for _ in range(N + 1)]
visited = [False] * (N + 1)

for i in range(link):
    a, b = map(int, input().split())
    network[a].append(b)
    network[b].append(a)

visited[1] = True
dfs(1)
print(count)

