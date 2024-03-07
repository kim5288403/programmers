from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0 
    maps = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, r)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    maps[i][j] = 0
                elif maps[i][j] != 0:
                    maps[i][j] = 1

    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    visited = [[False] * 102 for _ in range(102)]
    visited[cx][cy] = True
    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]
    
    queue = deque()
    queue.append((cx, cy))
    
    while queue:
        x, y = queue.popleft()
        
        if y == iy and x == ix:
            answer = maps[x][y] // 2
            break
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if not visited[nx][ny] and maps[nx][ny] == 1:
                visited[nx][ny] = True
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                 
    
    return answer 