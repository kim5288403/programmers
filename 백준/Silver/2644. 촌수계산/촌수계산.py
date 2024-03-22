import sys
N = int(sys.stdin.readline())
a, b = map(int,sys.stdin.readline().split())
M = int(sys.stdin.readline())
family = [[] for i in range(N+1)]
for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    family[x].append(y)
    family[y].append(x)
visited = [False for _ in range(N+1)]
result = []
def dfs(x, count):
    global flag
    visited[x] = True
    if x==b:
        flag=True
        print(count)
    for val in family[x]:
        if visited[val] == False:
            dfs(val,count+1)

flag=False
dfs(a,0)
if flag==False:
    print(-1)