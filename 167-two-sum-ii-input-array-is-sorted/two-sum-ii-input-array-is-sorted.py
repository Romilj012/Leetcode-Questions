class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(numbers):
            if target - num in hashtable:
                return [hashtable[target - num]+1, i+1]
            hashtable[numbers[i]] = i
        return []