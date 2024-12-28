class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        curr_max = values[0] - 1
        for i in range(1, len(values)):
            res = max(res, values[i] + curr_max)
            curr_max = max(values[i]-1, curr_max-1)
        return res


        
        