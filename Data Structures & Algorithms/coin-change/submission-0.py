class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount+1)
        dp[0] = 0

        for n in range(1,amount+1):
            for coin in coins:
                if n - coin >= 0:
                    dp[n] = min(dp[n], 1 + dp[n-coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1
