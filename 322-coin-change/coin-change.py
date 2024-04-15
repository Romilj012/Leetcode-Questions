class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount +1] * (amount+1)
        dp[0] = 0
        for amt in range(1,amount+1):
            for co in coins:
                if amt - co >=0:
                    dp[amt] = min(dp[amt], 1 + dp[amt-co])
        return dp[amount] if dp[amount] != amount + 1 else -1
            

        