class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countDict = Counter(nums)
        most_common_element, count = countDict.most_common(1)[0]
        if count > len(nums) // 2:
            return most_common_element
        return -1  


        