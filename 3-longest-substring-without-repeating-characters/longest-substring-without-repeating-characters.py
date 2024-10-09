class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        i = 0  # Left pointer of the window
        max_length = 0
        
        for j in range(len(s)):  # Right pointer of the window
            while s[j] in char_set:
                char_set.remove(s[i])
                i += 1  # Shrink the window from the left until s[j] is not in the set
            
            char_set.add(s[j])
            max_length = max(max_length, j - i + 1)  # Update the max length of the window
        
        return max_length

            

        