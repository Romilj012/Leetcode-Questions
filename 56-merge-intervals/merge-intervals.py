class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0
        while i < len(intervals)-1:
            if intervals[i+1][0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                intervals[i+1] = [
                    min(intervals[i+1][0], intervals[i][0]),
                    max(intervals[i+1][1], intervals[i][1]),
                ]
            i+=1  
        res.append(intervals[i])    
        return res
