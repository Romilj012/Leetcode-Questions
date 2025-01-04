class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            unique_palindromes = set()
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                l = s.find(ch, left, right)
                r = s.rfind(ch, left, right)

                if l != -1 and r != -1 and r - l > 1:
                    middle_chars = set(s[l + 1:r])
                    for middle_char in middle_chars:
                        unique_palindromes.add((ch, middle_char, ch))

            return len(unique_palindromes)
        return dp(0, len(s))
