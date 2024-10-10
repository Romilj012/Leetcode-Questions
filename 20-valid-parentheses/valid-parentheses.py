class Solution:
    def isValid(self, s: str) -> bool:
        par = {"}":"{", "]":"[", ")":"("}
        stack = []
        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            if i == "}" or i == "]" or i == ")":
                if stack and par[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True

        