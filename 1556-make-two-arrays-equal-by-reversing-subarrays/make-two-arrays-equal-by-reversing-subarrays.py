class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        
        count = {}
        
        for num in target:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for num in arr:
            if num in count:
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
            else:
                return False
        
        return not count
