import sys
from collections import deque
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(N)
    count = 0
    v[N] = 0

    while q:
        x = q.popleft()
        if x == K:
            count += 1
            continue

        for i in [x - 1, x + 1, x * 2]:
            if 0 <= i < 100001 and (v[i] == -1 or v[i] == v[x] + 1):
                v[i] = v[x] + 1
                q.append(i)


    print(v[K])
    print(count)

N, K = map(int, input().split())
v = [-1] * 100001

bfs()