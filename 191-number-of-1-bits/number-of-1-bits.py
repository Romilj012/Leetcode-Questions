class Solution:
    def hammingWeight(self, n: int) -> int:
        # def binary(a):
        #     s = 0
        #     for i in a:
        #         if i == '1':
        #             s+=1
        #     return s
        # return binary(bin(n)[2:])
        c =0
        while(n):
            if (n&1):
                c+=1
            n = n>>1
        return c  
        
        