import sys
input = sys.stdin.readline

def dfs(y, x, count):

    global result
    result = max(result, count)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R:
            if field[ny][nx] not in alphabet:
                alphabet.add(field[ny][nx])
                dfs(ny, nx, count + 1)
                alphabet.remove(field[ny][nx])


R, C = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]
visited = [[0] * C for _ in range(R)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = 0

alphabet = set(field[0][0])
dfs(0, 0, 1)

print(result)