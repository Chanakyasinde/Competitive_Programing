def largestAltitude(gain):
    n=len(gain)
    prefix=[0]* (n +1)
    for i in range(n):
        prefix[i]=prefix[i-1]+gain[i]
    return max(prefix)
