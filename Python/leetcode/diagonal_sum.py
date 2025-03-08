def calculate_diagonal_sum(matrix):
    n=len(matrix)
    total=0
    for i in range(n):
        total+=matrix[i][i]
        total+=matrix[i][n-1-i]
        if i==n-1-i:
            total-=matrix[i][i]
    return total
