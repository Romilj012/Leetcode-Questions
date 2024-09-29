class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # numSet = set()
        # for i in nums:
        #     if i not in numSet:
        #         numSet.add(i)
        #     else:
        #         return i
        #Floyd's cycle detection
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                break
        return slow

        