class Solution:
    def minimumLength(self, s: str) -> int:
        res = 0
        for count in Counter(s).values():
            if count % 2 == 0:
                res+=2
            else:
                res +=1
        return res            
        # c = Counter()
        # res = 0
        # for i in s:
        #     c[i]+= 1
        # for i, k in c.items():
        #     if k % 2 == 0:
        #         res+=2
        #     else:
        #         res +=1
        # return res
        

        