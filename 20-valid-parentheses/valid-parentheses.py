class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        my_dict = {')': '(', ']': '[', '}': '{'}
        for i in s:
            if i == "(" or i == "{" or  i == "[":
                stack.append(i)
            if i == ")" or i == "}" or  i == "]":
                if stack and my_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        return False

                    
                
        