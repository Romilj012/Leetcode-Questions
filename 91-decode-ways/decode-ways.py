class Solution:
    def numDecodings(self, s: str) -> int:
        @cache #key is parameters and value is the value when the function returns
        def dp(i):
            if i >= len(s): return 1
            elif s[i] == '0': return 0
            if i < len(s)-1 and int(s[i:i+2]) <=26:
                return dp(i+1) + dp(i+2)
            else:
                return dp(i+1)
        return dp(0)

    
  


        