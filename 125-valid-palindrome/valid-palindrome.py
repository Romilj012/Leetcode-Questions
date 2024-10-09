class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([char for char in s if char.isalnum()])
        if s[::-1].lower() == s.lower():
            return True
        return False
        