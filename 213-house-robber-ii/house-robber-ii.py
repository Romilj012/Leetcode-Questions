class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        dpSkipFirstHouse = []
        dpSkipLastHouse = []
        def houseRobber(n):
            if len(n) < 2:
                return n[0]
            dp = [n[0], max(n[0], n[1])]
            for i in range(2, len(n)):
                dp.append(max(dp[i-2] + n[i], dp[i-1]))
            return dp[len(n)-1]
        for i in range(len(nums)-1):
            dpSkipFirstHouse.append(nums[i]) 
            dpSkipLastHouse.append(nums[i+1])
        lootOfSkipFirst = houseRobber(dpSkipFirstHouse)
        lootOfSkipLast = houseRobber(dpSkipLastHouse)
        return max(lootOfSkipFirst, lootOfSkipLast)
       
        
        