class Solution:
    def canJump(self, nums: List[int]) -> bool:
        fI = len(nums) - 1
        for i in range(len(nums)-1, -1, -1): 
            if i + nums[i] >= fI:
                fI = i
        if fI:
            return False
        return True
        