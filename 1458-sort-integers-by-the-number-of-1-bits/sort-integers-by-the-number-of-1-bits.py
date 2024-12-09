class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        res = []
        def countBits(num):
            count = 0
            while num:
                num &=(num - 1)
                count +=1
            return count

        for num in arr:
            ones = countBits(num)
            res.append((ones, num))
        
        heapq.heapify(res)
        final = []
        while res:
            final.append(heapq.heappop(res)[1])
        return final
        


