def runningSum(nums):
    n=len(nums)
    prefix=[0]*n
    for i in range(n):
        if i==0:
            prefix[i]=nums[i]
        else:
            prefix[i]=prefix[i-1]+nums[i]
    return prefix
