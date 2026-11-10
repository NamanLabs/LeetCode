class Solution:
    def climbStairs(self, n: int, costs: list[int]) -> int:
        costs = [0] + costs
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for j in range(1, n + 1):
            dp[j] = min(dp[j], dp[j - 1] + 1)
            if j >= 2:
                dp[j] = min(dp[j], dp[j - 2] + 4)
            if j >= 3:
                dp[j] = min(dp[j], dp[j - 3] + 9)
            dp[j] += costs[j]
        return dp[n]
