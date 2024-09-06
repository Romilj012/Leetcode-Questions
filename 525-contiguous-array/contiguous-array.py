class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        #Base case
        res = 0
        one, zero = 0, 0
        a = {}
        for i, n in enumerate(nums):
            if n == 1:
                one += 1
            if n == 0:
                zero += 1
            if one - zero not in a:
                a[one-zero] = i
            if one == zero:
                res = one + zero
            res  = max(res, i - a[one-zero]) 
        return res
            
