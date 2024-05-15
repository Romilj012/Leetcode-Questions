class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            cooldown = dfs(i+1, buying)
            if buying:
                buy = dfs(i+1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i+2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        return dfs(0,True)


                

                

        # dp =[0 for i in range(len(prices))]
        # sell = 0
        # for i in range(len(prices)):
        #     if prices[i] > prices[i-1]:
        #         diff = prices[i] - prices[i-1]
        #         sell = sell + 1
        #         if sell > 0:
        #             dp.append(diff)
        #             dp[i] = dp[i] + diff
        #         sell -= 1
        #     print(dp)
        # return dp
        

        