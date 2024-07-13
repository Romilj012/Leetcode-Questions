class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # for i in range(len(nums)+1):
        #     if i not in nums:
        #         return i
        result = len(nums)
        for i in range(len(nums)):
            result += i - nums[i]
        return result

        