class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currentMax, currentMin = 1, 1
        for n in nums:
            if n == 0:
                currentMax, currentMin = 1,1 
            temp = n * currentMax
            currentMax = max(n * currentMax, n * currentMin, n)
            currentMin = min(temp, n * currentMin, n)
            result = max(result, currentMax)  
        return result