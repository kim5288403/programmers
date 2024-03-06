from collections import deque

def solution(begin, target, words):

    def bfs():
        queue = deque()
        queue.append([begin, 0])
        
        while queue:
            now, step = queue.popleft()
            
            print(now, step)
            
            if now == target:
                return step
            
            
            for word in words:
                count = 0 
                if now == word:
                    continue
                for i in range(len(now)):
                    if now[i] != word[i]:
                        count += 1
                        
                if count == 1:
                    queue.append([word, step + 1])
        
    if target not in words:
        return 0
    
    return bfs()