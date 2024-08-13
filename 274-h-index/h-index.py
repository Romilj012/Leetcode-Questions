class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = []
        for i in range(len(citations)):
            if citations[i] <= len(citations[i:]):
                res.append(citations[i])
            elif citations[i] >= len(citations[i:]):
                while citations[i]:
                    if citations[i] <= len(citations[i:]):
                        res.append(citations[i])
                    citations[i]-=1 
                continue
        return max(res) if res else len(citations) 
        
            

                    
