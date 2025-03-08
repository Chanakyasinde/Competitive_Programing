def pivotIndex(nums):
    n = len(nums)
    prefix = [0]*n
    for i in range(n):
        if i == 0:
            prefix[i] = nums[i]
        else:
            prefix[i] = prefix[i-1] + nums[i]
    for i in range(n):
        if i == 0:
            left_sum = 0 
        else:
            left_sum = prefix[i-1]
        right_sum = prefix[n-1] - prefix[i]
        if left_sum == right_sum:
            return i
    return -1
