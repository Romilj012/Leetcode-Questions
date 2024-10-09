class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = ''.join([char for char in s if char.isalnum()])
        # if s[::-1].lower() == s.lower():
        #     return True
        # return False
        newS = ""
        for c in s:
            if c.isalnum():
                newS += c.lower()
        return newS[::-1] == newS