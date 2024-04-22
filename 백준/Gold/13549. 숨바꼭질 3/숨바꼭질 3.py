import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)

    while q:
        s = q.popleft()
        if s == K:
            print(v[s])
            break

        if 0 <= s - 1 < limit and v[s - 1] == -1:
            v[s - 1] = v[s] + 1
            q.append(s - 1)
        if 0 <= s * 2 < limit and v[s * 2] == -1:
            v[s * 2] = v[s]
            q.appendleft(s * 2)  # 2* 가 다른 연산보다 더 높은 우선순위를 가지기 위함
        if 0 <= s + 1 < limit and v[s + 1] == -1:
            v[s + 1] = v[s] + 1
            q.append(s + 1)


N, K = map(int, input().split())
limit = 100001
v = [-1] * limit
v[N] = 0

bfs(N)
