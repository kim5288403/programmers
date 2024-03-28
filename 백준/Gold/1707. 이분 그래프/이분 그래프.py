import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(start, group):
    global flag
    v[start] = group

    for i in graph[start]:
        if not v[i]:
            dfs(i, -group)
        elif v[start] == v[i]:
            flag = True
            return


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    v = [False] * (V + 1)
    flag = False

    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1):
        if not v[i]:
            dfs(i, 1)

    if flag:
        print("NO")
    else:
        print("YES")
