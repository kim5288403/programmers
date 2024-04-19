from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    v[1] = True

    while q:
        dice = q.popleft()
        if dice == 100:
            print(arr[dice])
            break

        for i in range(1, 7):
            next_dice = dice + i
            if 0 < next_dice < 101 and not v[next_dice]:

                if next_dice in ladder.keys():
                    next_dice = ladder[next_dice]
                elif next_dice in snake.keys():
                    next_dice = snake[next_dice]

                if not v[next_dice]:
                    arr[next_dice] = arr[dice] + 1
                    v[next_dice] = True
                    q.append(next_dice)


N, M = map(int, input().split())
arr = [0] * 101
v = [False] * 101
ladder = dict()
snake = dict()

for _ in range(N):
    X, Y = map(int, input().split())
    ladder[X] = Y

for _ in range(M):
    U, V = map(int, input().split())
    snake[U] = V

bfs()