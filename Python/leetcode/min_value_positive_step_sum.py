def minStartValue(nums):
    prefix=[0]*n
    prefix[0]=n
    for i in range(1,n):
        prefix[i]=prefix[i-1]+nums[i]
