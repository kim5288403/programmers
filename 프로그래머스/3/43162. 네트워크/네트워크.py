def solution(n, computers):
    answer = 0
    visited = set()
    
    def dfs(node):
        visited.add(node)
        
        for nei in range(n):
            if nei not in visited and computers[node][nei]:
                dfs(nei)
    
    for start in range(n):
        if start not in visited :
            dfs(start)
            answer += 1
    
    return answer