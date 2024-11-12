# class Solution:
#     def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
#         items.sort()
#         beauty = 0
#         res = []
#         for i in queries:
#             for j in range(len(items)):
#                 if items[j][0] <= i:
#                     beauty = max(beauty, items[j][1])
#             res.append(beauty)
#         return res
            

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted([(q , i) for i , q in enumerate(queries)])
        max_beauty = [0] * len(queries)
        current_max = 0
        j = 0 
        for q, i in queries:
            while  j < len(items) and items[j][0] <= q:
                current_max = max(current_max, items[j][1])
                j += 1
            max_beauty[i] = current_max
        return max_beauty

        