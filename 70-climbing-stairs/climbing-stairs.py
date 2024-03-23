class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# another way

        # dp1, dp2 = 1,1
        # for i in range(0,n-1):
        #     temp = dp1
        #     dp1 = dp1 + dp2
        #     dp2 = temp
        # return dp1 
