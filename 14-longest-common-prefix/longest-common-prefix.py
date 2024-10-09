class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if len(strs) == 0:
        #     return ""
        # base = strs[0]
        # for i in range(len(base)):
        #     for word in strs[1:]:
        #         if(i == len(word) or word[i] != base[i]):
        #             return base[0:i]
        # return base
        ans=""
        strs=sorted(strs)
        first=strs[0]
        last=strs[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return ans
            ans+=first[i]
        return ans 