class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        seen = set()
        visitedSet = set()
        for num in nums:
            if num - k in seen:
                visitedSet.add((num - k, num))
            if num + k in seen:
                visitedSet.add((num, num + k,)) 
            seen.add(num)
        return len(visitedSet)           

            

            
            
            