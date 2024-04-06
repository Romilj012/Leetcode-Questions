class Solution:
    def rob(self, nums: List[int]) -> int:
        # oddSum = 0
        # evenSum = 0
        # maxSum = 0
        if len(nums) < 2:
            return nums[0]
        dp = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            dp.append(max(dp[i-2] + nums[i], dp[i-1]))
        return dp[len(nums)-1]
        #     if i % 2 !=0:
        #         oddSum = oddSum + nums[i]
        #     else:
        #         evenSum = evenSum + nums[i]
        # if oddSum > evenSum:
        #     return oddSum
        # elif oddSum < evenSum:
        #     return evenSum
        # else:
        #     return evenSum
