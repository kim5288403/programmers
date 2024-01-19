def solution(triangle):
    answer = 0
    sum_array = [[0 for _ in range(len(row))] for row in triangle]
    sum_array[0][0] = triangle[0][0]
    
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            sum_array[i + 1][j] = max(sum_array[i + 1][j], sum_array[i][j] + triangle[i + 1][j])
            sum_array[i + 1][j + 1] = max(sum_array[i + 1][j + 1], sum_array[i][j] + triangle[i + 1][j + 1])
            answer = max(answer, max(sum_array[i + 1][j], sum_array[i + 1][j + 1]))
    
    return answer