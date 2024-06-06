class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedList = nums1 + nums2
        mergedList.sort()
        length = len(mergedList)
        if length%2 == 0:
            index = int(length - 1) // 2
            return (mergedList[index] + mergedList[index+1]) / 2
        else:
            index = int(length - 1) // 2
            return mergedList[index]