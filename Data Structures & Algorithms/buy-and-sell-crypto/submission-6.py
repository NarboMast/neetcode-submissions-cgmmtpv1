class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n == 1: return 0

        dp = [0] * n

        for i in range(n-2, -1, -1):
            temp = dp[i+1] + (prices[i+1] - prices[i])

            dp[i] = max(temp, 0)

        return max(dp)
