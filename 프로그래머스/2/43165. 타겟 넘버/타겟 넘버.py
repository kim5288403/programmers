
def solution(numbers, target):
    answer = 0
    
    def dfs(index, amount):
        if index == len(numbers):
            if amount == target:
                nonlocal answer
                answer += 1
            return
        
        dfs(index + 1, amount + numbers[index])
        dfs(index + 1, amount - numbers[index])
        
    dfs(0, 0)
    
    return answer