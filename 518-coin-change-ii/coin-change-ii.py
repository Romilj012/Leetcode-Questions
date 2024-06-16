class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 0
        for i in range(len(coins)-1, -1 , -1):
            nextDp = [0] * (amount + 1)
            nextDp[0] = 1
            
            for amt in range(1,amount+1):
                nextDp[amt] = dp[amt]
                if amt - coins[i] >=0:
                    nextDp[amt] += nextDp[amt-coins[i]]
            dp = nextDp
        return dp[amount]