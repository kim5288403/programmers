import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(s):
    global count
    v[s] = True
    team.append(s)
    ns = arr[s]

    if v[ns]:
        if ns in team:
            count += len(team[team.index(ns):])
    else:
        dfs(ns)

T = int(input())

for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    v = [False] * (N + 1)
    count = 0

    for i in range(1, N + 1):
        if not v[i]:
            team = []
            dfs(i)

    print(N - count)
