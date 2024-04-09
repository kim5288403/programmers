import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def dfs(s):
    global count

    for i in arr[s]:
        if not v[i]:
            v[i] = True
            count += 1
            dfs(i)


C = int(input())
N = int(input())
arr = [[] for _ in range(C + 1)]
v = [False] * (C + 1)
count = 0

for i in range(N):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

v[1] = True
dfs(1)

print(count)
