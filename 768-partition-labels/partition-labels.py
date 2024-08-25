class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, c in enumerate(s):
            lastIndex[c] = i
        res = []
        size,end = 0,0
        for i, c in enumerate(s):
            size+=1
            end = max(end, lastIndex[c]) 
            if i == end:
                res.append(size)
                size = 0
        return res 
        



        # d = Counter(s)
        # finalList = []
        # res = "" 
        # for i in s:
        #     d[i] -= 1
        #     if d[i] == 0:
        #         finalList.append(len(res))
        #         res = ""      
        #     res+= i

            
        