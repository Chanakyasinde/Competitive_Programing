def sumOddLengthSubarrays(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        left = i+1
        right = n-i
        odd_count = ((left+1)//2)*((right+1)//2) + ((left//2)*(right//2))
        count += arr[i]*odd_count
    return count
