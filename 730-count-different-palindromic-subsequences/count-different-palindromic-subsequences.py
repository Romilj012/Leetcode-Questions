class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        
        # Initialize the DP table with -1
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        
        def help(i, j):
            if i > j:
                return 0
            if i == j:
                return 1  # Single character is always a palindrome
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                low, high = i + 1, j - 1
                while low <= high and s[low] != s[i]:
                    low += 1
                while low <= high and s[high] != s[j]:
                    high -= 1
                
                if low > high:  # No duplicate characters in the middle
                    dp[i][j] = help(i + 1, j - 1) * 2 + 2
                elif low == high:  # One duplicate character in the middle
                    dp[i][j] = help(i + 1, j - 1) * 2 + 1
                else:  # More than one duplicate character
                    dp[i][j] = help(i + 1, j - 1) * 2 - help(low + 1, high - 1)
            else:
                dp[i][j] = help(i + 1, j) + help(i, j - 1) - help(i + 1, j - 1)
            
            dp[i][j] = (dp[i][j] + MOD) % MOD  # Ensure non-negative modulo
            return dp[i][j]
        
        return help(0, n - 1)


