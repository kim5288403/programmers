def solution(tickets):
    answer = []
    visited = [False] * len(tickets)
    
    def dfs(a, lists):
        
        if len(lists) == len(tickets) + 1:
            answer.append(lists)
            return
        
        for i, ticket in enumerate(tickets):
            if ticket[0] == a and not visited[i]:
                visited[i] = True
                dfs(ticket[1], lists + [ticket[1]])
                visited[i] = False
    
    dfs("ICN", ["ICN"])
    answer.sort()
    
    return answer[0]