class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort intervals based on their end time
        intervals.sort(key=lambda x: x[1])
        print(intervals)
        # Initialize the count of non-overlapping intervals
        count = 0
        end = float('-inf')
        print(end)
        for interval in intervals:
            if interval[0] >= end:
                end = interval[1]
            else:
                count += 1
                
        return count
        