class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = 0
        dic = {}
        finalList = []
        heapList = []
        heapq.heapify(heapList)
        for point in points:
            dist = pow((pow(point[0], 2) + pow(point[1], 2)), 0.5)
            heapq.heappush(heapList, (dist, point))
        while k:
            dist, point = heapq.heappop(heapList)
            finalList.append(point)
            k-=1
        return finalList

