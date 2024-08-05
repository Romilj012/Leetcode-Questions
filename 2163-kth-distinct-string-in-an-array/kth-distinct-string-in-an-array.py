# class Solution:
#     def kthDistinct(self, arr: List[str], k: int) -> str:
#         result = []
#         for i in arr:
#             if arr.count(i)>1:
#                 continue
#             else:
#                 result.append(i)
#         if len(result) >=k:
#             return result[k-1]
#         else:
#             return ""

# from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        
        distinct = [i for i in arr if count[i] == 1]
        
        if len(distinct) >= k:
            return distinct[k - 1]
        else:
            return ""

        