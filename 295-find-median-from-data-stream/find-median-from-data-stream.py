class MedianFinder:

    def __init__(self):
        self.li = []
        

    def addNum(self, num: int) -> None:
        self.li.append(num)

    def findMedian(self) -> float:
        self.li.sort()
        n = len(self.li)
        if n % 2 != 0:
            return float(self.li[n // 2])
        else:
            mid1 = self.li[n // 2 - 1]
            mid2 = self.li[n // 2]
            return (mid1 + mid2) / 2

                
            



        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()