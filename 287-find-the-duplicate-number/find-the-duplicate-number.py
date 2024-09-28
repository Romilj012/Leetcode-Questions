class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSet = set()
        for i in nums:
            if i not in numSet:
                numSet.add(i)
            else:
                return i

        