def frogJump(heights):
    n = len(heights)
    dp = [-1] * n
    
    def recursive(index):
        if index == n - 1:
            return 0
        if dp[index] != -1:
            return dp[index]
        energy = float('inf')
        if index + 1 < n:
            energy = min(energy, abs(heights[index] - heights[index + 1]) + recursive(index + 1))
        if index + 2 < n:
            energy = min(energy, abs(heights[index] - heights[index + 2]) + recursive(index + 2))
        dp[index] = energy
        return dp[index]
    
    return recursive(0)
