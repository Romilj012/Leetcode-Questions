class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if (len(nums) == 1):
            return [nums.copy()]
        
        for i in range(len(nums)):
            num = nums.pop(0)
            perm = self.permute(nums)

            for p in perm:
                p.append(num)
            result.extend(perm)
            nums.append(num)
        return result