class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.temp = [0]*(len(self.nums)+ 1)
        for i in range(1, len(self.nums)+1):
            self.temp[i] = self.temp[i-1] + self.nums[i-1]
        
    def sumRange(self, left: int, right: int) -> int:
        return self.temp[right+1] - self.temp[left]


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)