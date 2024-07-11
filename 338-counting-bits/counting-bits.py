# class Solution:
#     def countBits(self, n: int) -> List[int]:
#         li = [0]
#         def countBit(i):
#             c = 0
#             while i:
#                 if i&1:
#                     c+=1
#                 i = i>>1
#             return c
#         for i in range(1,n+1):
#             a = countBit(i)
#             li.append(a)
#         return li

class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(i):
            c = 0
            while i:
                if i & 1:
                    c += 1
                i = i >> 1
            return c

        li = [countBit(i) for i in range(n + 1)]
        return li
        