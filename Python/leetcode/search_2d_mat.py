def searchMatrix(mat, target):
    n = len(mat)
    m = len(mat[0])
    low, high = 0, n * m - 1
    
    while low <= high:
        mid = (low + high) // 2
        mid_value = mat[mid // m][mid % m]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return False
