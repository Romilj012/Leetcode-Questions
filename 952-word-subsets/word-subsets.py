class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res = []
        c2 = defaultdict(int)
        for w in words2:
            cW = Counter(w)
            for c, cnt in cW.items():
                c2[c] = max(c2[c], cnt)
        for w in words1:
            cW = Counter(w)
            flag = True
            for c, cnt in c2.items():
                if cW[c] < cnt:
                    flag = False
                    break
            if flag:
                res.append(w)
        return res

             
        