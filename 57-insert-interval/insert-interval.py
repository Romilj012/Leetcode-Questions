class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Edge case: if intervals is empty
        if not intervals:
            return [newInterval]

        result = []
        i = 0

        # Add all intervals before the newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Merge intervals that overlap with newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # Add the merged newInterval
        result.append(newInterval)

        # Add remaining intervals after the newInterval
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
        