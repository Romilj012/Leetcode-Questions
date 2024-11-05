class Solution:
    def minChanges(self, s: str) -> int:
        j = 0
        count = 0
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                if i % 2 == 1:
                    count += 1
        return count 